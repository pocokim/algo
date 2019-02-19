slice , indexOf , for in , for of 삽질.. 
indexOf의 두번재인자로 시작 인덱스를 지정해줄 수 있다. 
for in의 i는 숫자가 아니라 문자로 key를 받는다. 따라서 i-1번째를 사용하고싶다면 이렇게 s[Number(i)-1] : i와 s[i]를 한꺼번에 사용가능 
for of 인덱스가 아닌 값을 이용하고 싶을때 사용 . 

function decodeString(s) {
 const stack =[];
    for( i in s){
        // console.log(s[i],i);
        const newS = s.slice(i);
        console.log(newS);
        
        const first = newS.indexOf('[');
        const next = newS.indexOf('[',first);
        console.log(first,next);
        const plusS = newS.slice(first,next)
        console.log(plusS);
        
        if(s[i] === "["){
            stack.push([s[Number(i)-1],plusS]); // for in 을 사용할때 i는 자동적으로 문자로 취급된다. 

        }
    }
    console.log(stack);

    var str = ""
        
        while(stack.length !== 0){
             const sentence = stack.pop()
             const cleanSen = sentence[1].split(']').join("")    
             
             console.log(cleanSen)
             const returnSen = cleanSen.repeat(sentence[0])
             console.log(returnSen);
             str += returnSen;
                
        }
    
    console.log(str);
        
    }


// function decodeString(s) {
//     const stack =[];
//     for( i in s){
//         console.log(s[i]);
//     }
    
// //     for( v of s){
// //         if(v === "["){
// //             console.log(v);
// //             stack.push(s[s.indexOf(v)+1])
            
// //         }
        
        
//         // s[s.indexOf(v)-1] 만큼 v다음의 문자를 넣는다. 
//         // if(v === "]"){stack.pop()}
//         console.log(stack);
//     }
// }
