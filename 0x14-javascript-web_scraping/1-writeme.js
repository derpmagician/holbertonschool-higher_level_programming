#!/usr/bin/node
// Read a file as arg

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

fs.writeFile(file, text, 'utf8', (error) => {
  if (error) console.log(error);
});
