#!/usr/bin/node
// Creates a Square class that extends Rectangle class

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
