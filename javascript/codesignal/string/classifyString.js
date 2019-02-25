// replaceAll 메소드 추가 
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

function classifyStrings(s) {
    // 1. 먼저 bad 인 경우를 골라낸다.
    // 2. bad로 걸러지지 않는 경우 + ?를 가지고 있는경우 mixed를 골라낸다.
    // 3. 나머지가 good 이다. 
    
    // bad 는 모음3개가 연속되거나, 자음5개가 연속되는 경우이다. 
    // mixed는 ?를 뺐을때 모음2개가 연속되거나, 자음4개가 연속되는 경우이다. -> splice로 처리하면 된다. 
    
    const vowels = ["*","a","e","i","o","u"];
    const consecutives = ['#', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w','x', 'y', 'z'];

    // bad 거르기 
    for( let i = 0; i<s.length; i++){
        if( vowels.includes(s[i]) && vowels.includes(s[i+1]) && vowels.includes(s[i+2]) ){
            return 'bad'
        }
    }
    for( let i = 0; i<s.length; i++){
        if( consecutives.includes(s[i]) && consecutives.includes(s[i+1]) && consecutives.includes(s[i+2]) 
           && consecutives.includes(s[i+3]) && consecutives.includes(s[i+4]) ){
            return 'bad'
        }
    }
    
    // mixed 거르기 
    s = s.replaceAll('?','*'); // 먼저 모두 모음으로 만들기
    
   for( let i = 0; i<s.length; i++){
        if( vowels.includes(s[i]) && vowels.includes(s[i+1]) && vowels.includes(s[i+2]) ){
            // bad 한번 더 거르기 
            return 'mixed'
        }
    }
    
    s = s.replaceAll('*','#');
   for( let i = 0; i<s.length; i++){
        if( consecutives.includes(s[i]) && consecutives.includes(s[i+1]) && consecutives.includes(s[i+2]) 
           && consecutives.includes(s[i+3]) && consecutives.includes(s[i+4]) ){
            // bad 한번 더 거르기 
            return 'mixed'
        }
    }
    
    // 나머지는 good 
    return 'good'
        
}
    

    
    
    
    
    


