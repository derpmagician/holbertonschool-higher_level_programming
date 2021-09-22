const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, data =>
  data.results.forEach(movie =>
    $('UL#list_movies').append(`<li>${movie.title}</li>`)));
