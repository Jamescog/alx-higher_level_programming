#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (target of list) {
    if (target === searchElement) {
      counter++;
    }
  }
  return counter
}
