const { Zilliqa } = require('@zilliqa-js/zilliqa')
const zilliqa = new Zilliqa('https://api.zilliqa.com');
fs = require('fs');

const getSubstate = async () => {
    const images = (await zilliqa.blockchain.getSmartContractSubState(
        '0x06f70655d4aa5819e711563eb2383655449f24e9', 'token_uris'
    ))['result']['token_uris']

    const metadata = (await zilliqa.blockchain.getSmartContractSubState(
        '0x06f70655d4aa5819e711563eb2383655449f24e9', 'metadata_map'
    ))['result']['metadata_map']

    const name = (await zilliqa.blockchain.getSmartContractSubState(
        '0x06f70655d4aa5819e711563eb2383655449f24e9', 'duck_name_map'
    ))['result']['duck_name_map']

    const result = Object.keys(images).map(key => (
        { 
            id: key,
            name: name[key],
            image: images[key],
            metadata: metadata[key] 
        }
    ))

    const names = Object.keys(images).map(key => (
        { 
            id: key,
            name: name[key]
        }
    ))
    
    console.log(result)

    fs.writeFile('currentducks2.json', JSON.stringify(result), function (err) {
        if (err) return console.log(err);
        console.log('Result > currentducks2.json');
    });

    fs.writeFile('names.json', JSON.stringify(names), function (err) {
        if (err) return console.log(err)
        console.log('Result > names.json')
    });
}


getSubstate()