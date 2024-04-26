import Person, {printName, printAge} from './module.js'

const user = new Person('Sally', 20);

console.log(user);
printName(user);
printAge(user);