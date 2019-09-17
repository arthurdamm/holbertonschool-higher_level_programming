#!/usr/bin/node
let n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
