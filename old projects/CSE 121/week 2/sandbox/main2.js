// // comparisons
// console.log('This is my message as a developer')


// console.log(5);
// console.log(5 == 5);
// console.log(5 === 5);
// console.log(5 >= 5);
// console.log(5 <= 5);
// console.log(5 > 5);
// console.log(5 < 5);
// console.log(5 >= 5 && 5 > 2);
// console.log(5 >= 5 && 5 < 2);
// console.log(5 >= 5 || 5 > 2);
// console.log(5 >= 5 || 5 < 2);
// let age = 12


// if (age < 6){
//     console.log("too young for school");
// } else if(age >= 6 && age <=18){
//     console.log("grade school")
// } else if(age > 18){
//     console.log("college")
// }





document.querySelector('h1').textContent = "New Output";

document.getElementById('main_title').textcontent = "Newer Output";

document.querySelector('#main_title').textContent = 'Newest Output';

document.querySelector('div').innerHTML = "<p>Para</p>";

//setAttribute method

let student = "images/student.jpg";

document.querySelector('img').setAttribute('src', student);
document.querySelector('img').setAttribute('alt', 'happy student');
document.querySelector('img').setAttribute('width', 400);

//create a new element using javascript
//1. create element, 2. add content, 3. add to the page
let newPara = document.createElement('p');
newPara.textContent = 'This is text for my paragraph';
document.body.appendChild(newPara);

let para = document.createElement('p1');
para.innerHTML += "<span>This is more information.</span>";


// Functions
function show() {
    console.log('this is it');
};

show();

function addIt(n1, n2){
    let answer = n1 + n2
    return( answer );
};

document.querySelector('#courses').textContent += addIt(3, 8);

//arrays

let classes = ['CSE121b', 'CIT354', 'WDD130', 'WDD230'];

console.log(classes);

console.log(classes[2]);

classes[2] = 'WDD330';

console.log(classes);
document.querrySelector('#courses').textContent = classes.join(', ');

//array methods

//push adds to the end of the array
classes.push('CIT222');
document.querySelector('#courses').textContent = classes.join(', ');

//shift takes off from the beginning
classes.shift()
document.querySelector('#courses').textContent = classes.join(', ');

let date = new Date();
let year = date.getFullYear(date);
console.log(date);
console.log(year);
