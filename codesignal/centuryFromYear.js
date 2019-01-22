function centuryFromYear(year) {
    if (year % 100 == 0) {
        return parseInt(year / 100)
    }
    else {
        return parseInt(year /100) +1
    }
    
}

console.log(centuryFromYear(1905))
console.log(typeof(1905))