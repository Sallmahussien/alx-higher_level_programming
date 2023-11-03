$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (obj) {
      $('#hello').text(obj.hello);
    }
  });
});
