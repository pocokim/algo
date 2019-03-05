function isCryptSolution(crypt, solution) {
    
    // 1. solution을 기준으로 dictionary를 만든다. 
    const table = {};
    for(let i =0; i<solution.length; i++){
        table[solution[i][0]] = solution[i][1];
    }
    console.log(table);
    
    
    // 2. 각 문자열(crypt[i])의 문자들을 table에 매치된 숫자로 바꾼다.  
    for(let i =0; i< crypt.length; i++){
        for(let j =0; j<crypt[i].length; j++){
            crypt[i] = crypt[i].replace(crypt[i][j],table[crypt[i][j]]); 
        }
    }
    
    // 3. 0이 leadingZero가 되는 경우를 제외한다.( 0 이아닌 0으로 시작하는 모든 문자열 ) 
    for( let i =0; i< crypt.length; i++){
        if(crypt[i].length !== 1 && crypt[i][0] === '0') return false 
    }
    
    // 4. 숫자로 바뀐 문자열을 계산한다. 
    if( parseInt(crypt[0]) + parseInt(crypt[1]) === parseInt(crypt[2])) return true
    else return false 
}

// 5. find 함수가 항상 좋은 함수가 아니다. 0으로 시작하는 문자열을 찾기 위해 find 함수를 사용하였으나 
// 0으로 시작하는 문자열을 찾기위해서는 주어진 solution에 0이 포함되어있어야했다. 
// 위 문제는 먼저 딕셔너리를 만들고, 딕셔너리에 맞게 변환하고 그 후에 0이 포함되어있는 경우를 처리한다! 와 같은 방식으로 구조를 잡아놓고 푸는것이 깔끔하다.  
// 
//     for(let i =0; i<solution.length; i++){
//         if(solution[i][1] === "0"){
//             haveZero = solution.find(element => element[1]==="0"); // 없을때 undefined 
//             const matchZero = haveZero[0];
//             if(crypt crypt[0][0] ===matchZero || crypt[1][0] ===matchZero ||crypt[2][0] === matchZero){ return false} 
//             // o이 1번만 있는 경우에는 false를 리턴하면 안됨. 

//         }
//     }
//     for(let i=0; i<solution.length; i++){
//         solution
//     }
   
    
    

