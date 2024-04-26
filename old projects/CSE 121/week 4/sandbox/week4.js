const car = {type: 'Fiat', model: '500', color: 'white'};

const person = {
    firstName: 'john',
    lastName: 'doe',
    age: 50,
    eyeColor: 'blue',


};

console.log(person['firstName']);

//A course object

const aCourse = {
    code: 'CSE121b',
    name: 'JavaScript Language',
    logo: 'images/JavaScript-logo.png',
    sections: [
        {sectionNum: 1, roomNum: "Stc 353",
        enrolled: 26, days: 'TTh', instructor: 'Bro T',},
        {sectionNum: 2, roomNum: "Stc 361",
        enrolled: 40, days: 'MW', instructor: 'Sis A',}
    ]

};

console.log(aCourse.name);

document.querySelector('#tittle').textContent = aCourse.name;

document.querySelector('img').setAttribute('src', aCourse.logo);
document.querySelector('img').setAttribute('alt', aCourse.name);

console.log(aCourse.sections[1].roomNum);

//adding an li with the first room number in array

document.querySelector('#sections').innerHTML = '<li>' + aCourse.sections[1].roomNum +'</li>';

//adding all the room numbers of the array

aCourse.sections.forEach(element => {
    document.querySelector('#sections').innerHTML += '<li>' + element.roomNum +'</li>'
});
aCourse.sections.forEach(element => {
    document.querySelector('#sections').innerHTML += '<li>' + element.instructor +'</li>'
});

// adding new li elements from scratch

aCourse.sections.forEach(function(item){
    let newListItem = document.createElement('li');
    newListItem.textcontent = item.roomNum;
    document.querySelector('#sections').appendChild(newListItem);
});

// let newListItem = document.createElement('li');
// newListItem.textcontent = aCourse.sections[0].roomNum;
// document.querySelector('#sections').appendChild(newListItem);