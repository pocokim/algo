//
// Definition for binary tree:
// function Tree(x) {
//   this.value = x;
//   this.left = null;
//   this.right = null;
// }


// 문제를 풀때 간과했던점. 언제 종료되게 할것인가? 이 문제는 재귀인가? 이런 생각을 안하고 풀었음.
// 어떻게 다음 노드로 넘어가게 할것인가? 를 traverseTree()를 통해 다음노드로 들어가게 했다.
// 그런데 종료조건을 설정해줘야했는데 언제 종료가 되는것이지? 처음에는 queue의 길이가 0 이되는곳에서 종료되어야하는줄알았는데... (이부분에서 한참해맴)
// 생각해보니 맨 아래의 traverseTree()를 탈출하는것이지 전체재귀를 탈출하는것은 아니었다. 그래서 처음 재귀가 시작됬던 부분에서 결과를 리턴하도록 했다.
// 
//  단순히 DFS처럼 재귀가 아니라 level별로 실행되게 하기위해서 어떻게 해야할지 고민을 해보았다. 재귀는 바로바로 안으로 들어가니까 쉬웠는데.. 
//  현재노드를 output에 넣고, 현재노드의 자식도 어딘가에 넣어야했는데.. 이부분에서 한참해맸다. 값을 추가하는건 두번해줄 필요없었고, 
//  현재노드를 output에 넣어주는 기능이 전담하면 되었고, 노드만 바꿔주면 되었다. 즉 순서를 고려해서 노드만 바꿔주면 되었다. 
//  큐에 노드를 넣어 순서를 기억하도록 하고, 큐에서 빼면서 노드를 이동하면 된다는걸 깨달았다.
//  이렇게 순서와 관련된 부분은 *스택이나, 큐를 사용하면되었다*. 


// 남의풀이: 해설을 보니 traverseTree를 돌리는게 아니라 현재 노드의 값이 있으면, 배열에 추가하는 작업을 반복하였다. 
// 굳이 traverseTree를 사용할필요가없었는데, 나는 DFS에 익숙해져서 재귀를 사용해야한다고 머릿속에 기억하고있었던것같다. 복습이 필요하다! 

const output = [];
const queue = [];
function traverseTree(t) {
    
    // 처음에 비어있을 수 있으므로 비어있는경우 바로 리턴 
    if(t === null) return output
    
    // 현재 노드의 값을 넣고, 다음노드의 값을 큐에 저장 
    output.push(t.value);
    if(t.left !== null){queue.push(t.left);}
    if(t.right !== null){queue.push(t.right);}
    
    /////////////////////////// 큐에서 빼면서 다음노드로 이동 <- 이부분 while문으로 짤수있을것같음.
    if(queue.length === 0){
        return
    }
    else{
        const shift = queue.shift();
        traverseTree(shift);       
    }
    /////////////////////////
    
    // 재귀가 다 끝난다음 결과를 리턴 
    return output
}

