
/**
 * CREATE TABLE nfds(
	ID INTEGER PRIMARY KEY NOT NULL,
  	Name TEXT,
  	Base TEXT,
  	Beak TEXT,
  	Eyes TEXT,
  	Hat TEXT,
  	Outfit TEXT,
  	BaseRarity REAL,
  	BeakRarity REAL,
  	EyesRarity REAL,
  	HatRarity REAL,
  	OutfitRarity REAL,
  	Background TEXT,
  	OverallRarity INTEGER
    );
 */

const sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('ducks.sqlite3');



for (let i = 1; i <= 8192; i++) {
    console.log(i)
    const thisDuckMetadata = require(`./FINAL/DUCK_`+String(i).padStart(4, "0"))
    const name = thisDuckMetadata['name']

    const base = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Base')['value']
    const beak = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Beak')['value']
    const eyes = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Eyes')['value']
    const hat = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Hat')['value']
    const outfit = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Outfit')['value']

    
    const baseRarityRaw = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Base Rarity')['value']
    const beakRarityRaw = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Beak Rarity')['value']
    const eyesRarityRaw = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Eyes Rarity')['value']
    const hatRarityRaw = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Hat Rarity')['value']
    const outfitRarityRaw = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Outfit Rarity')['value']

    const baseRarity = parseFloat(baseRarityRaw.replace('%', '')) / 100
    const beakRarity = parseFloat(beakRarityRaw.replace('%', '')) / 100
    const eyesRarity = parseFloat(eyesRarityRaw.replace('%', '')) / 100
    const hatRarity = parseFloat(hatRarityRaw.replace('%', '')) / 100
    const outfitRarity = parseFloat(outfitRarityRaw.replace('%', '')) / 100

    const background = thisDuckMetadata['attributes'].find(x => x.trait_type == 'Background')['value']
    const raw = baseRarity*beakRarity*eyesRarity*hatRarity*outfitRarity
    
    const overallRarity = (1/raw).toFixed()

    console.log(`ID ${i}`)
    console.log(`Name ${name}`)
    console.log(`Base ${base}`)
    console.log(`Beak ${beak}`)
    console.log(`Eyes ${eyes}`)
    console.log(`Hat ${hat}`)
    console.log(`Outfit ${outfit}`)
    console.log(`BaseRarity ${baseRarity}`)
    console.log(`BeakRarity ${beakRarity}`)
    console.log(`EyesRarity ${eyesRarity}`)
    console.log(`HatRarity ${hatRarity}`)
    console.log(`OutfitRarity ${outfitRarity}`)
    console.log(`Background ${background}`)
    console.log(`OverallRarity ${overallRarity}`)

    const insertQ = [i, name, base, beak, eyes, hat, outfit, baseRarity, beakRarity, eyesRarity, hatRarity, outfitRarity, background, overallRarity]

    let sql1 = 'INSERT INTO nfds VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    // let sql = 'INSERT INTO nfds VALUES (ID, Name, Base, Beak, Eyes, Hat, Outfit, BaseRarity, BeakRarity, EyesRarity, HatRarity, OutfitRarity, Background, OverallRarity)'

    
    // output the INSERT statement
   
    console.log(sql1);
    db.serialize(function(){
        db.run(sql1, insertQ, function(err){
            if(err) throw err;
        });
    });
    

}

