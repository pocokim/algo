
function findCloud(skyMap,i,j){
    const len = skyMap[0].length; 
    skyMap[i][j] = '0'
    if( i>0 && skyMap[i-1][j] === '1')  findCloud(skyMap,i-1,j);
    if( j>0 && skyMap[i][j-1] ==='1') findCloud(skyMap,i,j-1);
    if( i<len && skyMap[i+1][j] ==='1') findCloud(skyMap,i+1,j);
    if( j<len && skyMap[i][j+1] ==='1') findCloud(skyMap,i,j+1);
    // javascript 에서는 skyMap[-1]이런 값을 읽어올 수 없음.
    

}

function countClouds(skyMap) {
    let ans = 0;
    for(let i =0; i< skyMap.length; i++){
        for(let j=0; j<skyMap[0].length; j++){
            if(skyMap[i][j] === '1') {
                findCloud(skyMap,i,j)
                ans += 1;
            }
                    
        }
    }
    return ans
}

    