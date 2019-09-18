#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  console.log(('X'.repeat(n) + '\n').repeat(n));
} else {
  console.log('Missing size');
}
