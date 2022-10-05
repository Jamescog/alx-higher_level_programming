#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const myArr = process.argv.slice(2);
const a = Number(myArr[0]);
const b = Number(myArr[1]);
add(a, b);
