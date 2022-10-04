#!/usr/bin/node
const myArr = process.argv.slice(2);
const isInt = Number(myArr[0]);
const truthValue = isNaN(isInt);
if (truthValue) {
  console.log('Not a number');
} else {
  const num = parseInt(isInt, 10);
  console.log(num);
}
