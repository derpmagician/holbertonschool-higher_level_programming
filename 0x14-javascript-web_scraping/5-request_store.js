#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request.get(url).pipe(fs.createWriteStream(file));
