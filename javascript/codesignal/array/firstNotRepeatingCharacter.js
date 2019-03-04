function firstNotRepeatingCharacter(s) {
    const dic = {};
    for(let i =0; i<s.length; i++){
        if(!dic[s[i]]) dic[s[i]] =1;
        else dic[s[i]]++;
    }
    
    for( entries of Object.entries(dic) ){
        if(entries[1] === 1){ return entries[0]}
    }
    
    return '_'

}
