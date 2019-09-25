#!/usr/bin/node
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
