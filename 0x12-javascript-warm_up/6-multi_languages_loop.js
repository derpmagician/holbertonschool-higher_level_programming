#!/usr/bin/node
// prints 3 lines

const myArray = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let items in myArray) {
  console.log(myArray[items]);
}
