const $divBr = $('div#update_header');
const $headerElement = $('header');

$divBr.on('click', function () {
    $headerElement.text('New Header!!!');
})
