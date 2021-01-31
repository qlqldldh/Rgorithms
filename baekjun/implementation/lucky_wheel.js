const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []
let alphas = Array(26).fill(false)
let wheel
let flag = true

rl.on("line", function(line) {
    input.push(line)
}).on("close", function() {
    let [n, k] = input[0].split(" ").map((ele) => parseInt(ele))
    wheel = Array(n).fill("?")

    let point = 0
    for(let i=1;i<=k;i++){
        let [s, charac] = input[i].split(" ")
        point = (n + (point - parseInt(s)%n)) % n
        if((wheel[point] !== "?" || alphas[charac.charCodeAt(0) - 65]) && wheel[point] !== charac){
            flag = false
            break
        }
        wheel[point] = charac
        alphas[wheel[point].charCodeAt(0) - 65] = true
    }

    if(flag){
        let answer = []
        for(let i=0;i<n;i++){
            answer.push(wheel[(i+point)%n])
        }
        console.log(answer.join(""))
    }
    else{
        console.log("!")
    }
    process.exit()
})