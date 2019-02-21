  
  포함여부 찾는 로직     
  for(let i =0;i<ans.length;i++){
      if(ans[i]===s) return true;
  }
  return false;
  
  const checker = ans.filter(ele => ele === s); filter 함수 햇갈림 ㅜㅜ
  return (checker ? 1: -1) : 3항연산자 햇갈림 ㅠㅠ 
  if (checker) ? 1: -1 
  



 이렇게 되어있는 코드, 그냥 코드 위치만 수정하면 되는거였는데 ... 아래에서 빠지는 위치를 생각. 재귀를 하나 하나 벗어나는 생각이 전혀 떠오르지 못했다.
 함수가 실행되는 블록 ( 재귀가 끝난뒤의 함수의 위치와), path가 있는 위치를 잘 고려했어야 한다. ㅜㅜㅜ
function hasPathWithGivenSum(t, s) {
  
    path =[];
    ans = [];
  
  
    // 로직을 생각하고 함수를짤것 ㅠㅠ 앞에서도 
    function runPath(node){
        if(node === null ) return 
        path.push(node.value);
      
        if(node.left === null && node.right ===null){
            ans.push(path.reduce(getSum))
            path.pop();
        }
      
         
        if(node.left){
            runPath(node.left);
        }
        if(node.right){
            runPath(node.right);
        }

        //재귀함수의 동작 로직을 잘 생각하며 코드를 작성할것 
        //밑에서 하나하나 올라가는 로직을 생각했어야 ... 

    }
    runPath(t);
  