#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const myargs = process.argv.slice(2);
const mylength = myargs.length;

function compareN (a, b) {
  return b - a;
}

console.log(mylength < 2 ? 0 : myargs.sort(compareN)[1]);
