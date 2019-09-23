#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  newDict[value] = (newDict[value] || []).concat(key);
}
console.log(newDict);
