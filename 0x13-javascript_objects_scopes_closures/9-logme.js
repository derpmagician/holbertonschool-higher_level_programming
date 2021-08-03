#!/usr/bin/node
let order = 0;
exports.logMe = function (item) {
  console.log(`${order++}: ${item}`);
};
