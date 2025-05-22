// https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/javascript
const binaryArrayToNumber = arr => {
  // your code
//   parseInt takes string and returns an integer of the specified radix(base)
//   in this example, since we have binary, that means we need base 2
  return parseInt(arr.join(""), 2)
};