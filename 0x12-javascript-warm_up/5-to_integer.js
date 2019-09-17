#!/usr/bin/node
n = parseInt(process.argv[2])
if (n !== NaN)
  console.log('My number: ' + n)
else
  console.log('Not a number')
