#!/usr/bin/node
/*
  Write a script that computes the number of tasks completed by user id.
  The first arg is the API URL: https://jsonplaceholder.typicode.com/todos
  You must use the module request
*/

const request = require('request');
const taskDone = {};
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (err, resp, body) => {
  if (err || resp.statusCode !== 200) console.log(err);
  else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      const task = data[i];
      const user = data[i].userId;
      if (task.completed === true) {
        if (taskDone[user] !== undefined) {
          taskDone[user] += 1;
        } else {
          taskDone[user] = 1;
        }
      }
    }
    console.log(taskDone);
  }
});
