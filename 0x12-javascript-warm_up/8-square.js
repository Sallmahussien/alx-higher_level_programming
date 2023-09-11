#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    let row = '';
    for (let j = 0; j < argv[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
