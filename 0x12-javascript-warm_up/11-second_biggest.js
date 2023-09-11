#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length <= 1) {
  console.log(0);
} else {
  const integers = argv.map(Number).sort().reverse();
  console.log(integers[1]);
}
