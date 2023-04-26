const $divBr  = $('div#add_item');
const $ulElement = $('ul.my_list');

$divBr.on('click', function () {
    $ulElement.append('<li>Item</li>');
});

