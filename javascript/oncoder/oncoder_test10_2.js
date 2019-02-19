//핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
function solution(type){
    type.sort(function sortNumber(a,b) {
        return a - b;
    })


    const k = kCheck(type);


    var hash = {}
    for(let i =1; i<=k; i++){
        hash[i] = 0;
    }
    

    for(let i=0; i<type.length; i++){
        if( type[i] in hash){
            hash[type[i]] = hash[type[i]]+1
        }
    }
    
    console.log(hash)
    
    let ans = k
    for(let i=1; i<=k; i++){
        ans = ans* hash[i]

    }
    
    return ans
    
    
}

function kCheck(type){
    var n = 1;
    while(true){
        for(let i =0; i<type.length; i++){
            if(type.includes(n)){
                n++;
                if(i === type.length-1){return n-1}
                break;
            }
            else{return n-1}
        }
        
    }
}

solution([1,1,2,3,4,6])