let basesArr = []
let beaksArr = []
let eyesArr = []
let hatsArr = []
let outfitsArr = []
let backgroundArr = []

for (let i = 1; i <= 8192; i++) {
    console.log(i)
    const thisDuckMetadata = require(`./generatedMetadata/DUCK_`+String(i).padStart(4, "0"))

    const base = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Base')['value']
    const beak = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Beak')['value']
    const eyes = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Eyes')['value']
    const hat = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Hat')['value']
    const outfit = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Outfit')['value']
    const background = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Background')['value']

    if (basesArr.indexOf(base) == -1) basesArr.push(base)
    if (beaksArr.indexOf(beak) == -1) beaksArr.push(beak)
    if (eyesArr.indexOf(eyes) == -1) eyesArr.push(eyes)
    if (hatsArr.indexOf(hat) == -1) hatsArr.push(hat)
    if (outfitsArr.indexOf(outfit) == -1) outfitsArr.push(outfit)
    if (backgroundArr.indexOf(background) == -1) backgroundArr.push(background)
}

const basesJSON = basesArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(basesJSON)

const beaksJSON = beaksArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(beaksJSON)

const eyesJSON = eyesArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(eyesJSON)

const hatsJSON = hatsArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(hatsJSON)

const outfitsJSON = outfitsArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(outfitsJSON)

const backgroundJSON = backgroundArr.map(x => ({ name: x, value: x}) ).sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  })
console.log(backgroundJSON)

