#!/usr/bin/node
const list = require('./tests/100-data').list;
const newList = list.map((element, idx) => {
  return element * idx;
});

console.log(list);
console.log(newList);
