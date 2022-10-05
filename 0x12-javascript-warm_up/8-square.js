#!/usr/bin/node
const n = process.argv.slice(2)[0];
const char = 'X';
if (isNaN(n)) {
  console.log('Missing size');
} else {
  const square = char.repeat(n);
  for (let i = 0; i < n; i++) {
    console.log(square);
  }
}
