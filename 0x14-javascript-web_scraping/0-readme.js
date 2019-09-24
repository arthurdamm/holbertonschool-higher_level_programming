#!/usr/bin/node
// reads file passed as arg
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) console.log(error.stack);
  console.log(error || data);
});
