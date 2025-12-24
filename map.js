arr = [1,2,3,4,5,6,7]

arr.forEach((element) => {
    console.log(element*element)
});


let a = arr.map((element) => {
    return element+1
})

console.log(a)


let b = arr.filter((element)=> {
    return element>=5
})


console.log(b)



let c = arr.reduce((a,b)=>{
    return a + b
})

console.log(c)