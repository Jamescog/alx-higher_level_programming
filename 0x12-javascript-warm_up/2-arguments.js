#!/usr/bin/node
const count = process.argv.length;
if (count === 0) {
  console.log('No argument');
}
else if (count === 1) {
  console.log('Argument found');
}
else {
  console.log("Arguments found");
}
