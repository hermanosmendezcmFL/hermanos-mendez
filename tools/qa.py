# -*- coding: utf-8 -*-
"""Site QA: links, assets, duplicate meta, banned strings, EN/ES parity, sidebars, H1 casing.

Run from anywhere:  py tools/qa.py
"""
import io, re, json, os, glob, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
os.chdir(ROOT)


def load():
    return json.loads(io.open(ROOT / "tools" / "pages.json", encoding="utf-8").read())

issues = []


def add(kind, where, msg):
    issues.append((kind, where, msg))


files = [f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True)]
files = [f for f in files if not f.startswith("legacy/")]

# ---------------------------------------------------------------- link check
def exists(href):
    if href.startswith(("http://", "https://", "tel:", "mailto:", "#")):
        return True
    path = href.split("#")[0].split("?")[0]
    if not path.startswith("/"):
        return True
    p = path.lstrip("/")
    if path.endswith("/"):
        return os.path.isfile(os.path.join(p, "index.html"))
    return os.path.isfile(p)


for f in files:
    h = io.open(f, encoding="utf-8").read()
    for href in set(re.findall(r'href="([^"]+)"', h)):
        if not exists(href):
            add("DEAD LINK", f, href)
    for src in set(re.findall(r"url\('(/assets/[^']+)'\)", h)):
        if not os.path.isfile(src.lstrip("/")):
            add("MISSING ASSET", f, src)

# ------------------------------------------------------------- banned facts
BANNED = ["Sunbiz", "Bearss", "454-6897", "@hmcm", "@gmail", "L21000", "Dicipline", "An True",
          "Lorem", "TODO", "TBD", "coming soon", "Coming Soon"]
for f in files:
    h = io.open(f, encoding="utf-8").read()
    for b in BANNED:
        if b in h:
            add("BANNED TEXT", f, b)
    if re.search(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", h, re.I):
        add("EMAIL FOUND", f, "email address in markup")

# ------------------------------------------------------- pages.json structure
d = load()
DEFAULT_ASIDE = {"Related", "Relacionado", "Más", "More"}
for pg in d["pages"]:
    en, es, path = pg["en"], pg["es"], pg["en_path"]
    if len(en["paras"]) != len(es["paras"]):
        add("EN/ES MISMATCH", path, "paras %d vs %d" % (len(en["paras"]), len(es["paras"])))
    if len(en["links"]) != len(es["links"]):
        add("EN/ES MISMATCH", path, "links %d vs %d" % (len(en["links"]), len(es["links"])))
    for lang, blk in (("en", en), ("es", es)):
        if not blk.get("aside_h"):
            add("NO ASIDE HEADING", path, lang)
        elif blk["aside_h"] in DEFAULT_ASIDE:
            add("DEFAULT ASIDE HEADING", path, blk["aside_h"])
        for name, href in blk["links"]:
            if name.lower() in ("contact", "contacto"):
                add("CONTACT IN SIDEBAR", path, lang)
            if href.rstrip("/") == (path if lang == "en" else pg["es_path"]).rstrip("/"):
                add("SELF LINK IN SIDEBAR", path, href)
        n = sum(len(x) for x in blk["paras"])
        if n < 900:
            add("THIN COPY", path, "%s %d chars" % (lang, n))
    # EN headline title case: every significant word capitalised
    small = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or",
             "the", "to", "with", "from", "into", "over", "up", "vs"}
    words = re.findall(r"[A-Za-z][A-Za-z'’&-]*", en["h1"])
    bad = [w for i, w in enumerate(words)
           if w[0].islower() and w.lower() not in small and not w.isupper()]
    if bad:
        add("H1 NOT TITLE CASE", path, en["h1"] + "  -> " + ", ".join(bad))

# --------------------------------------------------------- duplicate meta
titles, descs = {}, {}
for f in files:
    h = io.open(f, encoding="utf-8").read()
    if 'http-equiv="refresh"' in h:
        continue
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    dsc = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    if t:
        titles.setdefault(t.group(1), []).append(f)
    if dsc:
        descs.setdefault(dsc.group(1), []).append(f)
for t, fs in titles.items():
    if len(fs) > 1:
        add("DUPLICATE TITLE", ", ".join(fs), t[:70])
for t, fs in descs.items():
    if len(fs) > 1:
        add("DUPLICATE DESC", ", ".join(fs), t[:70])

# ------------------------------------------------------------------- report
if not issues:
    print("QA clean")
else:
    order = {}
    for k, w, m in issues:
        order.setdefault(k, []).append((w, m))
    for k in sorted(order):
        print("== %s (%d)" % (k, len(order[k])))
        for w, m in order[k]:
            print("   %-52s %s" % (w, m))
