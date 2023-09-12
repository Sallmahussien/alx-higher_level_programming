#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((element, idx) => element * idx);

console.log(list);
console.log(newList);
