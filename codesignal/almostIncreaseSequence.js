
function almostIncreasingSequence(seq) {
    var bad=0
    for(var i=1;i<seq.length;i++) {
      if(seq[i]<=seq[i-1]) {
      bad++
      if(bad>1) return false
      if(seq[i]<=seq[i-2]&&seq[i+1]<=seq[i-1]) return false
      }
    }
    return true
  }
  
// 시간복잡도 
// function IsSorted(arr){
//     sorted = true;

//     for (var i = 0; i < arr.length - 1; i++) {
//         if (arr[i] >= arr[i+1]) {
//             sorted = false;
//             break;
//         }
//     }
    
//     return sorted
// }


// function almostIncreasingSequence(sequence) {

//     for(var i=0; i<sequence.length; i++){
//         var delElement = sequence.splice(i,1)[0]
 
//         if(IsSorted(sequence)){
//         return true        
//         }
//         sequence.splice(i,0,delElement)
            
//     }
    
    
    
//     return false
// }
