$(document).ready(function () {
  var autoplaySlider = $("#lightSlider").lightSlider({
    auto: true,
    loop: true,
    autoWidth: true,
    pauseOnHover: true,
    onBeforeSlide: function (el) {
      $("#current").text(el.getCurrentSlideCount());
    },
  });
  $("#total").text(autoplaySlider.getTotalSlideCount());
});

$(document).ready(function () {
  var autoplaySlider = $("#lightSliders").lightSlider({
    auto: true,
    loop: true,
    autoWidth: true,
    pauseOnHover: true,
    onBeforeSlide: function (el) {
      $("#current").text(el.getCurrentSlideCount());
    },
  });
  $("#total").text(autoplaySlider.getTotalSlideCount());
});

$(document).ready(function () {
  var autoplaySlider = $("#lightSliderss").lightSlider({
    auto: true,
    loop: true,
    autoWidth: true,
    pauseOnHover: true,
    onBeforeSlide: function (el) {
      $("#current").text(el.getCurrentSlideCount());
    },
  });
  $("#total").text(autoplaySlider.getTotalSlideCount());
});

$(document).ready(function () {
  var autoplaySlider = $("#lightSlidersss").lightSlider({
    auto: true,
    loop: true,
    autoWidth: true,
    pauseOnHover: true,
    onBeforeSlide: function (el) {
      $("#current").text(el.getCurrentSlideCount());
    },
  });
  $("#total").text(autoplaySlider.getTotalSlideCount());
});