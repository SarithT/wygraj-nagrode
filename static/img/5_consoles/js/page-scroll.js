! function (t) {
    "use strict";
    t("a.page-scroll").bind("click", function (a) {
        var o = t(this);
        t("html, body").stop().animate({
            scrollTop: t(o.attr("href")).offset().top
        }, 1250, "easeInOutExpo"), a.preventDefault()
    })
}(jQuery);
