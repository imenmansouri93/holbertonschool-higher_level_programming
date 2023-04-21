#!/usr/bin/node

function factoriel (a) {
  if (a === 1) {
    return a;
  }
  return a * factoriel(a - 1);
}
  const process = require('process');
  const args = process.argv;
  if (isNaN(args[2])) {
    console.log('1');
} else {
    const fac = args[2];
    console.log(factoriel(fac));
}
