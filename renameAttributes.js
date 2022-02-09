

const fs = require('fs')  
const Path = require('path')

const oldAttributeNames = JSON.parse(fs.readFileSync('./oldAttributeNames.json'))

oldAttributeNames.outfit.forEach(attr => {
    console.log(`${attr.value.split(' ').join('_')}`)
    console.log()
    const oldPath = `/home/ojgre/Documents/GitHub/Utility-DuckGenScripts/src/resources/outfits/${attr.value.split(' ').join('_')}.png`
    const newPath = `/home/ojgre/Documents/GitHub/Utility-DuckGenScripts/src/resources/croppedOutfits/${attr.label.split(' ').join('_')}.png`
    fs.copyFile(oldPath, newPath, (err) => {
        if (err) throw err;
        console.log(`${attr.value.split(' ').join('_')} was copied ${attr.label.split(' ').join('_')}.png`);
      });
})



