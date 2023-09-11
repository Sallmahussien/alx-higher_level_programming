#!/usr/bin/node

const argv = process.argv.slice(2).sort().reverse();
console.log(argv[1]);
