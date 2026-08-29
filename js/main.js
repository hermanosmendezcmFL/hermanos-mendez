(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#site-nav");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    nav.querySelectorAll(".nav-item.is-open").forEach(function (item) {
      item.classList.remove("is-open");
      var btn = item.querySelector(".nav-caret");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  }

  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav-item").forEach(function (item) {
    var btn = item.querySelector(".nav-caret");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      var open = !item.classList.contains("is-open");
      item.parentElement.querySelectorAll(".nav-item.is-open").forEach(function (other) {
        if (other !== item) {
          other.classList.remove("is-open");
          var ob = other.querySelector(".nav-caret");
          if (ob) ob.setAttribute("aria-expanded", "false");
        }
      });
      item.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeNav();
  });

  document.addEventListener("click", function (e) {
    if (!nav) return;
    if (!nav.contains(e.target) && toggle && !toggle.contains(e.target)) {
      if (window.matchMedia("(max-width: 900px)").matches) closeNav();
    }
  });
})();
