export default class Person {
    constructor(name, age){
        this.name = name,
        this.age = age
    }
}

export function printName(person){
    console.log(`User's name is ${person.name}`);
}
export function printAge(person){
    console.log(`User is ${person.age} years old`);
}