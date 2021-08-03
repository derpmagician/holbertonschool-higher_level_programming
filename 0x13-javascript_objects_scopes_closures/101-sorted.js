#!/usr/bin/node
// Concat two files

const { dict } = require('./101-data');

console.log(Object.entries(dict).reduce((accumulator, current) => {
  !accumulator[current[1]] ? accumulator[current[1]]  = [current[0]]: 0
  return accumulator;
}, {}));
