#!/usr/bin/node
// Prints all characters of a Star Wars movie:

const request = require('request');
const char_api = process.argv[2]
const starWarsUri = `https://swapi-api.hbtn.io/api/films/${char_api}`;

request(starWarsUri, function (error, response, body) {
  const characters = JSON.parse(body).characters;

  for (let char in characters) {
    request(characters[char], function (_err, _res, _body) {
      console.log(JSON.parse(_body).name);
    });
  }
});
