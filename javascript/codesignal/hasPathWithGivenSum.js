
function getSum(total, num) {
    return total + num;
  }  

function hasPathWithGivenSum(t, s) {
  
  path =[];
  ans = [];
  
  
  // 로직을 생각하고 함수를짤것 ㅠㅠ 앞에서도 
  function runPath(node){
      if(node === null ) return 
      path.push(node.value);
      // console.log(path);
         
      if(node.left){
          runPath(node.left);
      }
      if(node.right){
          runPath(node.right);
      }
      if(node.left === null && node.right ===null){
          ans.push(path.reduce(getSum))
      }
      path.pop();
      //재귀함수의 동작 로직을 잘 생각하며 코드를 작성할것 
      //밑에서 하나하나 올라가는 로직을 생각했어야 ... 

  }
  runPath(t);
  
  
  // in은 key 이고 of 가 값이다. 
  for ( el of ans){
      if(el === s) return true;
  }
  return false;
  
  

  
