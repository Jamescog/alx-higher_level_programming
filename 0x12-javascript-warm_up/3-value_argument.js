#!/usr/bin/node
const myArr = process.argv.slice(2);
if (typeof myArr[0] === 'undefined') {
  console.log('No argument');
} else {
  console.log(myArr[0]);
}
