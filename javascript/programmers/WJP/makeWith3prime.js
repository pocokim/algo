function solution(n) {
    var answer = 0;

    // n이하의 소수를 구하는 프로그램 알고리즘을 먼저 생각해야했다. 
    function getPrimeList(input){
        const primes = [];
        if( input < 2){ return primes}
        for( let i = 2; i<input+1; i++){
            let isPrime = true;
            for( let prime of primes){
                if( i % prime === 0 ){
                    isPrime = false;
                    break;
                }
                else if( prime > i*0.5){
                    break;
                }
            }
            if(isPrime){primes.push(i)}
        }
        return primes
    }
    
    const inputPrimes = getPrimeList(n);
    for(let i= inputPrimes.length-1; inputPrimes[i]>=parseInt(n/3); i--){ // 1. 소수중에 가장큰 수가 n/3보다 크고
        for(let j = 0; inputPrimes[j] <= (n - inputPrimes[i])/2; j++){ // 2. 소수중에 가장 작은 수가 n/3보다 작을때 
             const middleNum = n-inputPrimes[i]-inputPrimes[j];
            if( middleNum > inputPrimes[j] && middleNum <inputPrimes[i] ){ // 중간숫자가 맞는지 확인하고
                if( inputPrimes.includes(middleNum)){ // 소수인지 확인 
                    answer += 1;
                }
            }
        }
    } 
    return answer;
}

console.log(solution(33));
console.log(solution(9));