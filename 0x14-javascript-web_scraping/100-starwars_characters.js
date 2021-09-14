#!/usr/bin/node
// Prints all characters of a Star Wars movie:

const request = require('request');
const charApi = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${charApi}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;

  for (const char in characters) {
    request(characters[char], function (_err, _res, _body) {
      console.log(JSON.parse(_body).name);
    });
  }
});
