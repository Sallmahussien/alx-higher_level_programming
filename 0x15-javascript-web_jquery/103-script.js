$(document).ready(() => {
  // Function to fetch translation and update the result
  const fetchTranslation = () => {
    const langCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/', { lang: langCode }, (lang) => {
      $('#hello').text(lang.hello);
    });
  };

  // Bind the click event to the button
  $('#btn_translate').click(() => {
    fetchTranslation();
  });

  // Bind the keyup event to the input field
  $('#language_code').keyup((event) => {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
