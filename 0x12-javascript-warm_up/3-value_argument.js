#!/usr/bin/node
let s;
if (process.argv.length < 3) {
  s = 'No argument';
} else {
  s = process.argv[2];
}
console.log(s);
