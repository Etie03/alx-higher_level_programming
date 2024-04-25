#!/usr/bin/node
let m;
if (process.argv.length < 3) {
  m = 'No argument';
} else if (process.argv.length === 3) {
  m = 'Argument found';
} else {
  m = 'Arguments found';
}
console.log(m);
