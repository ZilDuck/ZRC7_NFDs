const fs = require('fs')


const state = fs.readFileSync('./currentducks2.json')
const stateDucks = JSON.parse(state)
 

const findMetadataFromURI = (uri) => {
    const generatedMetadataDir = './FINALGENERATEDMETADATA'
    const fileNames = fs.readdirSync(generatedMetadataDir)
    for (i in fileNames) {
        const thisDuckPath = `${__dirname}/FINALGENERATEDMETADATA/${fileNames[i]}`
        
        const thisDuckData = JSON.parse(fs.readFileSync(thisDuckPath))
        if(thisDuckData["transparent"] == uri) {
            return thisDuckData
        }
    }
}

for (i in stateDucks) {
    const id = parseInt(i) + 1
    const thisDuck = stateDucks.find(duck => duck["id"] == id)
  
    const thisURI = 'ipfs://' + thisDuck["image"].split("https://gateway.pinata.cloud/ipfs/")[1]
    console.log(`duck ${id}: ${thisURI}`)
    const duckData = findMetadataFromURI(thisURI)
    
    console.log(`${id}: ${duckData["transparent"]}`)
    //fs.writeFileSync(`./FINALMATCHEDMETADATA/DUCK_${String(id).padStart(4, '0')}.json`, JSON.stringify(duckData, null, 2))
}
 