#!/usr/bin/node

const argv = process.argv.map(Number).slice(2).sort().reverse();

if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(argv[1]);
}
