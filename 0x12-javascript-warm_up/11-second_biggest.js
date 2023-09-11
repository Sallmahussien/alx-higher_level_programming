#!/usr/bin/node

const argv = process.argv.slice(2).sort().reverse();

if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(Number(argv[1]));
}
