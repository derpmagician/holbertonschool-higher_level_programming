#!/usr/bin/node
// Prints the title of a Star Wars movie equal to a given integer.

const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;

request(url, function (_error, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
