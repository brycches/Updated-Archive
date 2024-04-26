console.log('This is my message as a developer')

console.log(typeof 42);
console.log(typeof "abc");
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof { a: 1 });
console.log(typeof [1, 2, 3]);
console.log(typeof function hello() {});



var adult = true; //var is the same as let but it makes a variable global not local. let outside of a scope will also make it global.

let myName = "Bob";
let age = 24;
const PROFESSION = 'instructor';

if (adult) {
  
}
console.log(PROFESSION)
console.log(myName);
// Bob

console.log(age);
// Error!

adult = 6;

console.log(adult);

let myVariable = 4;
let newnum = 'foo' + 3;
console.log(myVariable + 3);

myVariable = 6

console.log(myVariable)

const one = 1;
const two = "2";
const three = "e";
let result = one + two;
console.log(result);
output("ln7", result);

result = one + parseInt(two);
output("ln10", result);
console.log(result);
// We didn't get any output from line 9 above. What change would you need to make to get it to work? Make the change. Hint...in the bottom left corner of the window there is a button 'Console'. Click it.

// what about multiplication?
result = one * two;
output("ln16", result);
console.log(result);
// was the result what you expected?

// what about this? Explain what is happening. What does NaN mean?
result = one * three;
output("ln21", result);
console.log(result);
// let's try changing the value of two
too = 4;

result = one + two;
output("ln27", result);
console.log(result);
// did we get the value we expected? Why didn't it work?
// try adding 'use strict'; to the first line of our code then look at the console again. Fix the error.

const myArray = [1,2,3,5];
//add the number 4 to the end of the array

console.log(myArray);
// it would be nice if our numbers were in the correct order. We will learn how to sort later, for now let's remove the last two items in the array and then add them back in the correct numerical order.




console.log(myArray);


// The code below is used to aid in displaying the results.
function output(line, content) {
  const outputElement = document.querySelector(".output");
  outputElement.innerHTML += `<p>${line} : ${content}</p>`;
}
