#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(arg => parseInt(arg));
  integers.sort((x, y) => y - x); // Sort in descending order
  console.log(integers[1]); // The second biggest integer
}
