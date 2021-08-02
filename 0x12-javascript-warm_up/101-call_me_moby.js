#!/usr/bin/node
// Write a function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  while (x > 0) theFunction x--;
};
