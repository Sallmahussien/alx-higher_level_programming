#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf-8', (error, data) => {
  if (error) console.log(error);
  else console.log(data);
});
