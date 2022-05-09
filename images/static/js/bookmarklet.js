(function () {
  let jquery_version = "3.4.1";
  let site_url = "https://127.0.0:8000/";
  let static_url = site_url + "static/";
  let min_width = 100;
  let min_height = 100;

  function bookmarklet(msg) {
    // the bookmarklet code should be inserted here.
  }

  // verify whether jQuery is loaded.
  if (typeof jQuery !== "undefined") {
    bookmarklet();
  } else {
    // check conflicts.
    let conflict = typeof window.$ != "undefined";
    // create the script that points to googles api.
    let script = document.createElement("script");
    script.src =
      "//ajax.googleapis.com/ajax/libs/jquery" +
      jquery_version +
      "/jquery.min.js";

    // adds the script to the head for processing.
    document.head.appendChild(script);

    // determine a wainting form unti the script be loaded.
    let attempts = 15;
    (function () {
      // checks again whether jQuery is undefined.
      if (typeof window.jQuery == "undefined") {
        if (--attempts > 0) {
          // calls itself im some milliseconds.
          window.setTimeout(arguments.callee, 250);
        } else {
          // Excess of tries to load, send an error.
          alert("An error ocurred while loading jQuery");
        }
      } else {
        bookmarklet();
      }
    })();
  }
})();
