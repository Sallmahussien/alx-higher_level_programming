#!/usr/bin/node

const argv = process.argv;
const number = parseFloat(argv[2]);

console.log(isNaN(number) ? 'Not a number' : `My number: ${Math.floor(number)}`);
