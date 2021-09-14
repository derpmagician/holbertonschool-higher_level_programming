#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const tasks = JSON.parse(body);
  const finished = {};

  for (const task of tasks) {
    if (task.completed === true) {
      if (!(task.userId in finished)) {
        finished[task.userId] = 1;
      } else {
        finished[task.userId]++;
      }
    }
  }
  console.log(finished);
});
