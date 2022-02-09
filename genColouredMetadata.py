import json
from os import write
import sys
import glob
import shutil
from textwrap import indent

oldAttrFile = open('./oldAttributeNames.json')
oldAttributes = json.load(oldAttrFile)
oldAttrFile.close()

coloursFile = open('./colours.json')
coloursPerDuck = json.load(coloursFile)
coloursFile.close()

IPFSFile = open('./newimagehashes.json')
IPFS = json.load(IPFSFile)
IPFSFile.close()

compressedHashesFile = open('./compressedHashes.json')
compressedHashes = json.load(compressedHashesFile)  
compressedHashesFile.close()

transparentImagesFile = open('./data.json')
transparentImages = json.load(transparentImagesFile)
transparentImagesFile.close()

currentducksFile = open('./currentducks2.json')
currentducks = json.load(currentducksFile)
currentducksFile.close()

missingArweave = []

def readOldMetadata (id):
    filename = "./metadata/DUCK_" + str("{0:0=4d}".format(id)) + ".json"
    
    f = open(filename)
    data = json.load(f)

    f.close()
    return data

def getNewAttributeName (type, original):
    for attribute in oldAttributes[type]:
        if original == attribute["value"]:
            return attribute["label"] 
    
    print(type, original)
    sys.exit()

def getOldColour (id):
    for duck in coloursPerDuck["ducks"]:
        if duck["id"] == id:
            return duck["colour"]
    
    print("Failed getting background colour for " + str(id))
    sys.exit()

def getIPFSImage (id):
    for duck in IPFS:
        if duck["id"] == "DUCK_" + str("{0:0=4d}".format(id)):
            return duck["hash"]
    
    print("Failed getting arweave url for " + str(id))
    sys.exit()
    
def getName (id):
    for duck in currentducks: 
        print(duck)
        if duck['id'] == str(id):
            return duck["name"]
    print("Failed getting name for " + str(id))
    sys.exit()

def getCompressedHash (id):
    id = "DUCK_" + str("{0:0=4d}".format(id))
    for duck in compressedHashes["ducks"]:
        if duck["id"] == id:
            return duck["hex"]
    
    print("Failed getting hash " + str(id))
    sys.exit()


def genNewMeta(id):
    oldAttributes = readOldMetadata(id)


    base = getNewAttributeName("bases", oldAttributes["duck_base_name"])
    beak = getNewAttributeName("beaks", oldAttributes["duck_beak_name"])
    eyes = getNewAttributeName("eyes", oldAttributes["duck_eyes_name"])
    hat = getNewAttributeName("hats", oldAttributes["duck_hats_name"])
    outfit = getNewAttributeName("outfit", oldAttributes["duck_outfit_name"])
    baseRarity = oldAttributes["duck_base_occurrence_chance"]
    beakRarity = oldAttributes["duck_beak_occurrence_chance"]
    eyesRarity = oldAttributes["duck_eyes_occurrence_chance"]
    hatsRarity = oldAttributes["duck_hats_occurrence_chance"]
    outfitRarity = oldAttributes["duck_outfit_occurrence_chance"]

    colour = getOldColour(id)

    ipfsHash = getIPFSImage(id)

    pinata = transparentImages[str(id)]["uri"]
    ipfshash = pinata.split("https://gateway.pinata.cloud/ipfs/")[1]

    compressedHash = getCompressedHash(id)
    s3url =  "https://d22rrd5cdtalai.cloudfront.net/DUCK_" + str("{0:0=4d}".format(id)) + "_" + compressedHash + ".png"
    print(s3url)
    
    filename = "./FINALGENERATEDMETADATA/DUCK_" + str("{0:0=4d}".format(id)) + ".json"
     

    with open(filename, "w") as write_file:
        result = {        
            "resource": ipfsHash, #arweave coloured
            "resource_mimetype": "image/png",
            "attributes": 
            [ 
                {
                    "display_type" : "string",
                    "trait_type": "Base", 
                    "value": base
                }, 
                {
                    "display_type": "string",
                    "trait_type": "Beak",
                    "value":  beak
                },
            
                {
                    "display_type" : "string",
                    "trait_type": "Eyes", 
                    "value": eyes
                },
                {
                    "display_type" : "string",
                    "trait_type": "Hat", 
                    "value": hat
                },
                {
                    "display_type" : "string",
                    "trait_type": "Outfit", 
                    "value": outfit
                },
                {
                    "display_type" : "string",
                    "trait_type": "Background", 
                    "value": colour
                },
                {
                    "display_type" : "string",
                    "trait_type": "Base Rarity", 
                    "value": baseRarity
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Beak Rarity", 
                    "value": beakRarity
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Eyes Rarity", 
                    "value": eyesRarity
                },
                {
                    "display_type" : "string",
                    "trait_type": "Hat Rarity", 
                    "value": hatsRarity
                },
                {
                    "display_type" : "string",
                    "trait_type": "Outfit Rarity", 
                    "value": outfitRarity
                }
            ],
            "transparent": "ipfs://" + ipfshash,
            "quick_resource": s3url
        }
        print(result)
        json.dump(result, write_file, indent=2)
        
    return




id = 0
#genNewMeta(3955)
for filename in glob.glob('./generated/generated/DUCK_*.png'):
    id = id + 1
    print(id)
    genNewMeta(id)
        


# ================================================================

for missing in missingArweave:
    print(missing)

