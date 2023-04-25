/*Uses thee jquery API to change the color of the DIV#red_header to red onclick*/

$('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
});