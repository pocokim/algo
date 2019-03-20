function climbingStaircase(n, k) {

    const answer = []
    function goNext(n, load) {


        if (n === 0) {
            answer.push(load)
            return
        }
        else if (n < 0) { return }
        
        else { 
            for (let i = 1; i <= k; i++) {
                const copyLoad = load.slice() // copy 
                copyLoad.push(i) // update copyLoad

                goNext(n - i, copyLoad);
            }
        }

    }

    goNext(n, [])
    return answer

}
