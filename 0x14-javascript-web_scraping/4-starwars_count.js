#!/usr/bin/node
// Prints the title of a Star Wars movie equal to a given integer.

const request = require('request');
const Wedge = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];

request(url, function (error, _res, body) {
  if (error) { return; }

  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const char of film.characters) {
      if (char === Wedge) {
        count++;
      }
    }
  }
  console.log(count);
});
