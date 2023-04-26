const $headerElement = $('header');
const $divHeader = $('div#toggle_header');

$divHeader.on('click', function () {
  const currentClass = $headerElement.attr('class')
    if (currentClass === 'green') {
        $headerElement.toggleClass(`${currentClass} red`);
    }
    if (currentClass === 'red') {
        $headerElement.toggleClass(`${currentClass} green`);
    }
      
})

