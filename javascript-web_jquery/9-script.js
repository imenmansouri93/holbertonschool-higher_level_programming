const $divHeader = $('div#hello');
const Uri = 'https://stefanbohacek.com/hellosalut/?lang=fr';

$get(Uri, function (data) {
    $divHeader.text(data.hello);
});
