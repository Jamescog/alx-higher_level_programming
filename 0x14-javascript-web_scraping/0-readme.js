#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, (err, data) => {
  console.log(err || data.toString());
});
