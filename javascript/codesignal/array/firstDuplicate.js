function firstDuplicate(a) {
    const answer = [-1];
    const countMap = a.reduce(function(accum,value,idx){
       accum[value] = accum[value] + 1 || 1; 
        if(accum[value] === 2) answer.push(value);
        return accum;
    },{});
    
    if(answer.length ===1) return answer[0]
    else return answer[1]
}
    // reduce 안쓰고 for문으로 , 있는지 없는지 유무로 파악할 수 있음.
    // function firstDuplicate(a) {
    //   var dictionary = {};

    //   for(var i = 0; i < a.length; i++) {
    // if(dictionary[a[i]] !== undefined)
    //      return a[i];
    // else
    //    dictionary[a[i]] = i;
    //   }

    //   return -1;
    // }