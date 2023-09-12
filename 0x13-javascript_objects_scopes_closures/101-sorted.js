#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (!newDict[dict[key].toString()]) {
    newDict[dict[key].toString()] = [];
  }
  newDict[dict[key].toString()].push(key);
}

console.log(newDict);
