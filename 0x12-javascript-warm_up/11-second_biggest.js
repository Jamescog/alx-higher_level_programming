#!/usr/bin/node
const myArr = process.argv.slice(2);
const n = myArr.length;
if (n <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < n; i++) {
    myArr[i] = Number(myArr[i]);
  }
  myArr.sort();
  myArr.reverse();
  console.log(myArr[1]);
}
