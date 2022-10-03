#!/usr/bin/node
const myArgs = process.process.slice(2);
let n = myArgs.length;
if (n === 0) {
  console.log('No argument');
} else if (n === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
