process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split('\n');
    const lenT1 = Number(n[0]);
    const lenT2 = Number(n[lenT1+1]);
    const table1 = [];
    const table2 = [];
    
    for(let i=2; i<=lenT1; i++){
        table1.push(n[i]);
    }
    table1.sort((a, b) => a.split(' ')[0] - b.split(' ')[0])
    table1.unshift(n[1]);
    // console.log(table1);
    
    for(let i=lenT1+3; i<=lenT1+lenT2+1; i++){
        table2.push(n[i]);
    }


    table2.sort((a, b) => a.split(' ')[0] - b.split(' ')[0])
    table2.unshift(n[lenT1+2]);
    // console.log(table2);
    
    const item = table2[0].split(' ').length;
    // console.log(item);
    
    table2[0] = table2[0].slice(2);
    table1[0] += table2[0]
    for(let i=1; i<table1.length; i++){
        var found = false;
        for(let j =1; j<table2.length; j++){
            if(table1[i][0] === table2[j][0]){
                
                table2[j] = table2[j].slice(1)
                table1[i] += table2[j];
                
                found = true;
                break;
            }

        }
        if(found === false){
            table1[i] += ' NULL'.repeat(item-1);
        }
    }
    console.log(table1.join("\n"))

});