function nextLarger(a) {
    const answer = [];

    for( let i =0; i<a.length; i++){
        // a[i]가 비교되야할 배열 생성
        const toSee = a.slice(i);
        // console.log('지금비교하고있는 대상숫자 :',a[i],'비교해야할 배열',toSee);
        
        // 비교대상 배열돌면서 큰 수가 있으면 큰수 추가 , 없으면 - 1 추가 
        for( let j =0; j<toSee.length; j++){
            if(toSee[j]>a[i]) {
            answer.push(toSee[j]);
            break;
            }
            else if(a[i] === Math.max( ... toSee)) {
            answer.push(-1);
            break;
            }
        }
        // console.log(answer)
        
    }
    return answer
}
