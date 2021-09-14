#!/usr/bin/node
// Read a file as argunment

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) => {
  console.log(error || data);
});
