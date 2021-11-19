// const num = 1
// console.log(num)

// const arr1 = ['asdasd', 'asdasd', 'adssa']
// const arr2 = [1, 2, 3, 4, 6]
// const arr3 = [true, false]

// console.log(arr1)
// console.log(arr2)
// console.log(arr3)

// arr1.push(11)
// console.log(arr1)

// let arr = [
//     [1, 2, 3, 4],
//     [7, 3, 3, 3],
//     [91, 2, 1, 2]
// ]

// arr[0].shift()
// console.log(arr)

// arr[1].unshift(4, 5)
// console.log(arr)

// for (let i = 0; i < arr.length; i++) {
//     const student = arr[i]
//     console.log(
//         `haro ${student[0]}.
//             ${student[1]}.
//             ${student[2]}`
//     )
// }

// class warra {
//     abilities = ['atk', 'fed']
//     name = "warr"
//     kurasu = "war"

//     show() {
//         console.log(this.abilities)
//     }
// }

// const warria = new warra()
// warria.show()


// function curryFunction(a, b) {
//     const c = a + b
//     return function (d) {
//         console.log(c + d)
//     }
// }
// curryFunction(15, 78)(43)
// // const arrowCurryFunction = (a, b) => (d) => (a + b + d)
// const arrowCurryFunction = (a, b) => ({ a, b })
// console.log(arrowCurryFunction(1, 2))


// const anot = (a, b) => (c, d) => (a + b) - (c + d)
// const aad = anot(32, 41)(14, 22)
// console.log(aad)

// name = "rukhas"
// role = "asdasd"
const obj = {
    name: "asd",
    role: "full",
    age: 62
}
// const { name: fullname, role: job,  } = obj
const { name, role, age } = obj
console.log(obj['name'] + ' ' + obj['role'])
// console.log(fullname, job, age)
console.log(name, role, age)


const students = [
    ["asdasd", "jobu1", true],
    ["tetetete", "jobu2", true],
    ["asdfdfdfdfasd", "jobu3", true]
]

const [nico, ricky, fauzi] = students

const [namaeee, ...fauzis] = fauzi

console.log({ namaeee, fauzis })