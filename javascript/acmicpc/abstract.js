let input = 'abcdefg';
const arr = input.split('');
console.log(arr);

function reverse(str){
    return str.split('').reverse().join('');
}

input = reverse(input);

console.log(input);