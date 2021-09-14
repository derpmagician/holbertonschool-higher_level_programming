#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request.get(url).pipe(fs.createWriteStream(file));
