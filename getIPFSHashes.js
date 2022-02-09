const public = "2ed6e02efc6e762d354d"
const private = "894e271425a0260f8f5ff01bcd358e55d191ada83ddf8c09e69958e77c1113b7"

const pinataSDK = require('@pinata/sdk');
const pinata = pinataSDK(public, private);

const ducksDirectory = __dirname + '/generated/generated/'
console.log(ducksDirectory)

const fs = require('fs')
const path = require('path')
let ducksToUpload = []

fs.readdir(ducksDirectory, async function(err, files) {
    if (err) {
      return console.log('Unable to scan directory: ' + err);
    }

    files.forEach(async function(file) {
        let numberStr = path.parse(file).name;
        ducksToUpload.push(numberStr)
    })
    console.log(ducksToUpload)
    getAllPinned()
})


let results = []

const getPinned = async (id) => {
    const metadataFilter = {
        'type': 'ZRC6',
        'name': id

    };
    
    const filters = {
        metadata: metadataFilter,
        status : 'pinned',
        pinStart: '2021-12-04T00:00:00.000Z',
    };

    await pinata.pinList(filters).then(async (result) => {
        result['rows'].forEach(x => {
            console.log(id + " " +"ipfs://" + x.ipfs_pin_hash)
            results.push({"id": id, "hash": "ipfs://" + x.ipfs_pin_hash})
        })
    }).catch(async (err) => {
        console.log('err')
        console.log(err);
        await sleep(5000)
        await getPinned(id)
    });
}

const sleep = async (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms))
}

const getAllPinned = async () => {

    for (let i = 1216; i <= 2045; i++) { 
        await sleep(750)
        console.log("REGEN_" + String(i).padStart(4, "0"))
        await getPinned("REGEN_" + String(i).padStart(4, "0"))
        
    }

    const data = JSON.stringify(results, null, 4);

    fs.writeFile('newregenhashes2.json', data, (err) => {
        if (err) {
        throw err;
        }
        console.log('JSON data is saved.');
    });
}


