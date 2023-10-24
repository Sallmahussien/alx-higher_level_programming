#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error) console.log(error);
  else console.log(`code: ${response.statusCode}`);
});
