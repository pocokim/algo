
function sumOfTwo(a, b, v) {
    
    var c = a.concat(b);
    c.sort((a,b)=>a-b)
    start = 0;
    end = c.length-1;
    

    let ans1 = null;
    let ans2 = null;
    for(let i =0; i<c.length; i++){
        let sum = c[start]+c[end]
        if(sum < v)start++
        else if(sum> v)end--
        if(c[start]+c[end] === v){
            ans1 = c[start];
            ans2 = c[end];
            break;
        }

    }
        

    
    var d = a.map(function(item){ return parseInt(item)})
    var e = b.map(function(item){ return parseInt(item)})
    console.log(d,e)
   
    
    if(d.includes(ans1) && d.includes(ans2)) return false
    if(e.includes(ans1) && e.includes(ans2)) return false
    if(ans1 !==null && ans2 !== null) return true
}
    
    