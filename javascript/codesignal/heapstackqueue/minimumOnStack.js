function minimumOnStack(operations) {
    const stack = [];
    const answer = [];
    const min = [];
    
    for(let i =0; i<operations.length; i++){
        let [words, number] =  operations[i].split(" ")
        let last = min.length -1 
        number = parseInt(number);
        if(words === 'push'){
            stack.push(number)
            if(min.length === 0){
                min.push(number);
            }
            else if(min[last] > number) min.push(number)
        }
        if(words === 'min'){answer.push(min[last])}
        if(words === 'pop'){
            const popedValue = stack.pop();
            if( popedValue === min[last]){
                min.pop();
            } 
        }

    }
    return answer;
}
