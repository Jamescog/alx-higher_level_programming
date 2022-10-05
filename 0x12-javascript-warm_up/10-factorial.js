#!/usr/bin/node
const n = Number(process.argv.slice(2)[0]);
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
