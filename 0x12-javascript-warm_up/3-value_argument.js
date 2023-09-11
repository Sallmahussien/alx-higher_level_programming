#!/usr/bin/node

const argv = process.argv;
console.log(!argv[2] ? 'No argument' : argv[2]);
