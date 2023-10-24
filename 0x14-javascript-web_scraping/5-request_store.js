#!/usr/bin/node

const args = process.argv;
const request = require('request');
const fs = require('fs');

request(args[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    fs.writeFile(args[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
