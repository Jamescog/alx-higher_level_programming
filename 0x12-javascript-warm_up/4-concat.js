#!/usr/bin/node
const myArr = process.argv.slice(2);
const count = myArr.length;
if (count === 0) {
  console.log('undefined is undefined');
} else if (count === 1) {
  console.log(myArr[0] + ' is undefined');
} else {
  console.log(myArr[0] + ' is ' + myArr[1]);
}
