#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    const results = {};
    const todosData = JSON.parse(body);

    todosData.forEach((todo) => {
      if (!results[todo.userId] && todo.completed) results[todo.userId] = 1;
      else if (results[todo.userId] && todo.completed) results[todo.userId]++;
    });

    console.log(results);
  }
});
