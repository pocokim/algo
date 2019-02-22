
function getSum(total, num) {
    return total + num;
  }  

// 재귀함수의 기본작동 : 재귀함수가 종료되면 그 윗단계의 재귀함수를 실행한다. 
function hasPathWithGivenSum(t, s) {
  
  path =[];
  ans = [];
  
  
  function runPath(node){
      if(node === null ) return // 종료조건 
      
      path.push(node.value);
         
      
      // 현재 node의 자식이 있는 지 확인, runPath(node)에서 runPath(node.left)로 들어간다고 해서 runPath함수가 종료되는것이 아님. 
      // 자식의 runPath 가 실행된 후에 29~34line의 작업을 수행 
      if(node.left){
          runPath(node.left);
      }
      if(node.right){
          runPath(node.right);
      }
      
      // leaf 노드를 만났을때 수행되어야 하는 작업 
      if(node.left === null && node.right ===null){
          ans.push(path.reduce(getSum))
      }
      
      // runPath 함수가 종료되기 직전에 일어나야 하는 작업 
      path.pop();



  }
  runPath(t);
  return ans.includes(s)
  
}