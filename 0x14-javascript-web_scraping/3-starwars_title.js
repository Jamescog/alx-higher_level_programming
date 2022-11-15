#!/usr/bin/nodejs
const request = require('request');
const num = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${num}`;
request(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
