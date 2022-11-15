#!/usr/bin/nodejs
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, function (err, file) {
  if (err) throw err;
});
