function solution(people, tshirts) {
    var answer = 0;
    function sortNumber(a,b) {
        return a - b;
    }
    people.sort(sortNumber) // 오름차순
    tshirts.sort(sortNumber) // 오름차순 
    // console.log(people,tshirts);
    const fp = people.filter(person => {
        for(let item of tshirts){ // tshirt 배열에서 찾는 경우 배열 값변경
            if(person <= item){
                const it = item 
                tshirts.splice(tshirts.indexOf(item),1)
                // console.log(tshirts);
                return person <= it
            }
        }
        
        
    });
    return fp.length;
}

console.log(solution([2,3],[1,2,3]));