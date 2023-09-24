
let add: Function = (a: number, b: number) => a + b

let operation = (a: number, b: number, fn: Function) => fn(a, b)

let resultByAdd = operation(2,2, add)
let directOperation = operation(2,2, (a: number, b: number) => a + b)

console.log(`Result 1: ${resultByAdd}\nResult 2: ${directOperation}`)