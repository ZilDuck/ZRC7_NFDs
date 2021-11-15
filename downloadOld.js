const fs = require('fs');
const client = require('https');

let currentDucks = []
fs.readFile('./regen.json', 'utf8',  (err, data) => {
    if (err) {
        console.log(`Error reading file from disk: ${err}`);
    } else {
        currentDucks = JSON.parse(data);
        downloadDucks(currentDucks)
    }
})

async function downloadDucks (currentDucks) {
    console.log(currentDucks[8])
    for (let i in currentDucks) {
        let newLink = currentDucks[i].uri
        console.log(`${i} - Downloading ${newLink}`)
        await downloadImage(newLink, `./allDucks/REGEN_${String(i).padStart(4, '0')}.png`)
    }
}

async function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

async function downloadImage(url, filepath) {
    await wait(100)
    
    url = url.replace('gateway.pinata.cloud', 'gateway.ipfs.io')
    console.log(url)
    return new Promise((resolve, reject) => {
        client.get(url, async(res) => {
            if (res.statusCode === 200) {
                res.pipe(fs.createWriteStream(filepath))
                    .on('error', reject)
                    .once('close', () => resolve(filepath));
            } else {
                // Consume response data to free up memory
                res.resume();
                reject(new Error(`Request Failed With a Status Code: ${res.statusCode}`));
                await wait(2500)
                url = url.replace('https://gateway.pinata.cloud/', 'https://ipfs.io/')
                downloadImage(url, filepath)
            }
        });
    });
}

