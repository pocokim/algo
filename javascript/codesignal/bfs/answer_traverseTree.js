//
// Definition for binary tree:
// function Tree(x) {
//   this.value = x;
//   this.left = null;
//   this.right = null;
// }
function traverseTree(t) {
    var result = [];
    var nodes = [];
    nodes.push(t);
    
    // BFS
    while(nodes.length > 0) {
        var node = nodes.shift();
        if(node !== null) {
            nodes.push(node.left);
            nodes.push(node.right);          
            result.push(node.value);
        }
    }
    
    // DFS
    // while(nodes.length > 0) {
    //     var node = nodes.pop();
    //     if(node !== null) {
    //         nodes.push(node.right);          
    //         nodes.push(node.left);
    //         result.push(node.value);
    //     }
    // }
    
    return result;
}
