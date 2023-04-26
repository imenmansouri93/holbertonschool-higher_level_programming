const $ulHeader  = $('ul#list_movies');
const Uri = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(Uri, function (data) {
    for (const film of data.results){
        $ulHeader.append(`<li>${film.title}</li>`);
    }
});