function containsDuplicates(a) {

    var obj = a.reduce(function(accum,curValue){
        if(accum[curValue]) accum[curValue]++
        else accum[curValue] = 1; 
        return accum
    },{})
    
    for( var key in obj){
        if(obj[key]>1) return true
    }
    return false 
}