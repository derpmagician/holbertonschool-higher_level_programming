#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');
const arg = process.argv.slice(2)

const file1 = fs.readFileSync(arg[1], 'utf8');
const file2 = fs.readFileSync(arg[2], 'utf8');

fs.writeFileSync(arg[3], file1 + file2);
