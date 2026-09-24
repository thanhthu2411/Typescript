import {Invoice} from './classes/invoice.js'
import {Payment} from './classes/Payment.js'
import type { HasFormatter } from './interfaces/HasFormatter.js'

let character = "annaa"

const inputs = document.querySelectorAll("input")

console.log(inputs)

inputs.forEach(input => {
    console.log(input)
})

let age = 30
let isBlackBelt = false

const fun = (diameter: number) => {
    return diameter * Math.PI
}

console.log(fun(1))

// arrays, objects

let names = ["anna", "bin", "clara"]

    // names.push(1) - ERRORS
names[0] = "ann"


let mixed = ["ken", 4, 9, "anna", true] 
// if we declare an array of mixed types, then it allows mixed types

let ninja = {
    name: "mario",
    belt: "black",
    age: 30
}

// once we define an obj, we can't add additional property to it: ninja.skills = "fighting"

ninja = {
    name: "ryu",
    belt: "white",
    age: 98
} // the new obj properties need to match the one declared, same structure


// EXPLICIT TYPES

let person: string
let score: number
let isStudent: boolean

score = 100
isStudent = true

let students: string[] = []

students.push("anna")

// arrays of union type
let mixed_students: (string|number)[] = []
mixed_students.push(24)
mixed_students.push("24")

let student_id: number|string
student_id = 123
student_id = "S-123"

// objects
let studentOne: object
studentOne = {name: "anna", age: 30}

let studentTwo: {
    name: string,
    age: number,
    isStudent: boolean
}

studentTwo = {name: "thu", age: 23, isStudent: true}

// DYNAMIC TYPES
let a: any = 25
a = true

let mixed_dynamic_array: any[] = []
mixed_dynamic_array.push(true)
mixed_dynamic_array.push(24)

let mixed_dy_obj: {name: any, age: any}

// FUNCTIONS
let greet = () => {
    console.log("hello")
}

let greet2: Function

greet2 = () => {
    console.log("hello")
}

const add = (a :number, b: number, c?: number|string): void => {
    console.log(a+b)
} // the ? after c says that the param is optional

add(5, 10)

const minus = (a :number, b: number, c?: number|string): number => {
    return a - b
}

// function signatures
let greet3: (a: string, b: string) => void

greet3 = (name, greeting) => {
    console.log(name, greeting)
}

let log: (obj: {name: string, age: number}) => void

type person = {name: string, age: number}

log = (student: person) => {
    console.log(student.name)
}

// TYPE ALIASES

type StringOrNum = string | number;

const logDetails = (user: {name: string, uid: StringOrNum}) => {
    console.log(`${user.name}`)
}

// DOM & TYPE CASTING
const anchor = document.querySelector('a')

console.log(anchor?.href)

const form = document.querySelector(".new-item-form") as HTMLFormElement
console.log(form.children)

// CLASSES
const inOne = new Invoice("anna", "shoes", 50)
const inTwo = new Invoice("bob", "bags", 150)

let invoices: Invoice[] = []
invoices.push(inOne)
invoices.push(inTwo)

console.log(invoices)

// INTERFACES: enforce certain structure of a class/object

interface IsPerson {
    name: string
    age: number
    
    speak(a: string): void
    spend(a: number): number
}

const me: IsPerson = {
    name: "a",
    age: 12,

    speak(text) {
        console.log(text)
    },

    spend(amount) {
        return amount
    }
}

// INTERFACES AND CLASSES
let docOne: HasFormatter
let docTwo: HasFormatter

docOne = new Invoice("a", "wee", 564)
docTwo = new Payment("ab", "work", 574)

let docs: HasFormatter[] = []
docs.push(docOne)
docs.push(docTwo)

console.log(docs)
