#!/usr/bin/node
// prints 3 lines

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const items in myArray) {
  console.log(myArray[items]);
}
