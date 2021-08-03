#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');
const myarg = process.argv.slice(1);

const file1 = fs.readFileSync(myarg[1], 'utf8');
const file2 = fs.readFileSync(myarg[2], 'utf8');

fs.writeFileSync(myarg[3], file1 + file2);
