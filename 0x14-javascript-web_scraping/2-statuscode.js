#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, (_error, response, body) => {
  if (!_error) {console.log('code:', response && response.statusCode)};
});
