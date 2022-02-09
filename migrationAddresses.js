const fs = require('fs')
let addresses = []
for (let i = 0; i < 44; i++) {
    addresses.push('0x24DdeDbf3A3DF608f4C9fbF56153866947e1b159')
}

console.log(addresses)
const data = JSON.stringify(addresses, null, 4);
fs.writeFileSync('./addresses.json', data, 'utf8');
