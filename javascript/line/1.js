process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    for(let w=parseInt(Math.sqrt(data)); w>0; w-- ){
        if(data/w === parseInt(data/w)){
            const h = data/w;
            console.log(Math.abs(w-h));
            break;
        }
    }
    
});