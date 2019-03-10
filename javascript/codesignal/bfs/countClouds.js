
function findCloud(skyMap,i,j){
    const ylen = skyMap[0].length;
    const xlen = skyMap.length; 
    skyMap[i][j] = '0'
    if( i>0 && skyMap[i-1][j] === '1' ) findCloud(skyMap,i-1,j);
    if( j>0 && skyMap[i][j-1] === '1' ) findCloud(skyMap,i,j-1);
    if( i<xlen-1 && skyMap[i+1][j] === '1' ) findCloud(skyMap,i+1,j);
    if( j<ylen-1 && skyMap[i][j+1] === '1' ) findCloud(skyMap,i,j+1);
    
}
    //if( i>0 ){
    //    if(skyMap[i-1][j] === '1') findCloud(skyMap,i-1,j);
    //} 
    // if( j>0 ){
    //     if( skyMap[i][j-1] ==='1') findCloud(skyMap,i,j-1);
    // } 
    // if( i<xlen-1 ){
    //     if( skyMap[i+1][j] ==='1') findCloud(skyMap,i+1,j);
    // } 
    // if( j<ylen-1 ){
    //     if( skyMap[i][j+1] ==='1') findCloud(skyMap,i,j+1);
    // 
    // javascript 에서는 skyMap[-1]이런 값을 읽어올 수 없으므로
    // 처음 if문에서 i,j의 범위값을 조절 
    



function countClouds(skyMap) {
    let ans = 0;
    for(let i =0; i< skyMap.length; i++){
        for(let j=0; j<skyMap[0].length; j++){
            if(skyMap[i][j] === '1') {
                console.log(i,j)
                findCloud(skyMap,i,j)
                ans += 1;
            }
                    
        }
    }
    return ans
}

    