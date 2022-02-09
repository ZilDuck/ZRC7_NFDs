const public = "2ed6e02efc6e762d354d"
const private = "894e271425a0260f8f5ff01bcd358e55d191ada83ddf8c09e69958e77c1113b7"

const pinataSDK = require('@pinata/sdk');
const pinata = pinataSDK(public, private);


const { DateTime, Interval, Duration } = require('luxon');
const fs = require('fs')
const path = require('path')

const uploadDuck = async (file, id) => {
    console.log(`\nUploading ${file}   ID: ${id} ...\n`)

    const readableStreamForFile = fs.createReadStream(file);
    const options = {
        pinataMetadata: {
            type: "ZRC6",
            name: id
        }
    }

    await pinata.pinFileToIPFS(readableStreamForFile, options)
        .then((result) => {
            console.log(`\nSuccess for ${id}`)
            console.log(result);
            console.log(`https://cloudflare-ipfs.com/ipfs/${result.IpfsHash}`)
            console.log(`Writing file...`)
            let resHash = 'ipfs://' + result.IpfsHash
            console.log({"id": id, "hash": resHash})
            let old = JSON.parse(fs.readFileSync('./newregenhashes2.json'))
            old["hashes"].push({"id": id, "hash": resHash})
            fs.writeFileSync('./newregenhashes2.json', JSON.stringify(old))
        }).catch((err) => {
            console.log(err);
            uploadDuck(file, id)
        })
}

const ducksDirectory = __dirname + '/generated/generated/'
console.log(ducksDirectory)


let ducksToUpload = []
/* const notUploaded = ["DUCK_2659",
    "DUCK_3768",
    "DUCK_5908",
    "DUCK_7451",
    "DUCK_7870"] */

fs.readdir(ducksDirectory, async function(err, files) {
    if (err) {
      return console.log('Unable to scan directory: ' + err);
    }

    files.forEach(async function(file) {
        let directory = ducksDirectory + file;
        //console.log('add to array file: ' + directory);
        let numberStr = path.parse(file).name;
        //if (notUploaded.indexOf(numberStr) != -1) {
        if (numberStr.includes('REGEN')) {
            console.log('added')
            console.log({numberStr, directory})
            ducksToUpload.push({numberStr, directory})
        }
        //}
    })
    await pin()
})

const pin = async () => {
    console.log('pin')
    const start = DateTime.now();

    for (const i in ducksToUpload) {
        if (i > 1213) {
            const end = DateTime.now();
            console.log('\n===========================================');

            const diff = Interval.fromDateTimes(start, end)
                .toDuration(['days', 'hours', 'minutes', 'seconds'])
                .toObject();

            const estimatedMillis = (diff.seconds / (i / ducksToUpload.length)) * 1000;
            const duration = Duration.fromMillis(estimatedMillis).toFormat('hh:mm:ss');

            console.log(
            `Elapsed: ${Duration.fromMillis(diff.seconds * 1000).toFormat(
                'hh:mm:ss',
            )}\nEstimated: ${duration} `,
            );

            await uploadDuck(ducksToUpload[i].directory, ducksToUpload[i].numberStr)
        }
    }
}


