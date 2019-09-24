#!/usr/bin/node
// makes get request for SW movie id
const request = require('request');
const find = '/people/18/';
request(process.argv[2], function (error, response, body) {
  try {
    !error && body && console.log(JSON.parse(body).results.filter(film => film.characters.includes(find)).length);
  } catch (error) {
  }
});
