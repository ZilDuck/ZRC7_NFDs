import json
import sys

oldAttrFile = open('./oldAttributeNames.json')
oldAttributes = json.load(oldAttrFile)
oldAttrFile.close()

coloursFile = open('./colours.json')
coloursPerDuck = json.load(coloursFile)
coloursFile.close()

arweaveFile = open('./arweave.json')
arweaveImages = json.load(arweaveFile)
arweaveFile.close()

transparentImagesFile = open('./data.json')
transparentImages = json.load(transparentImagesFile)
transparentImagesFile.close()

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

def getArweaveImage (id):
    for duck in arweaveImages:
        if duck["name"] == "DUCK_" + str("{0:0=4d}".format(id)) + ".png":
            return duck["dataTxId"]
    
    print("Failed getting arweave url for " + str(id))
    sys.exit()



def genNewMeta(id):
    oldAttributes = readOldMetadata(id)

    base = getNewAttributeName("bases", oldAttributes["duck_base_name"])
    beak = getNewAttributeName("beaks", oldAttributes["duck_beak_name"])
    eyes = getNewAttributeName("eyes", oldAttributes["duck_eyes_name"])
    hat = getNewAttributeName("hats", oldAttributes["duck_hats_name"])
    outfit = getNewAttributeName("outfit", oldAttributes["duck_outfit_name"])

    colour = getOldColour(id)

    arweaveHash = getArweaveImage(id)

    pinata = transparentImages[str(id)]["uri"]
    ipfshash = pinata.split("https://gateway.pinata.cloud/ipfs/")[1]

  
    filename = "./generatedMetadata/DUCK_" + str("{0:0=4d}".format(id)) + ".json"

    with open(filename, "w") as write_file:
        result = {        
            "name": "Cloud Quackers",
            "description": "Non-Fungible Ducks",
            "resource": "https://arweave.net/" + arweaveHash, #arweave coloured
            "resource_mimetype": "image/png",
            "external_url": "https://duck.community",
            "external_description": "Non-Fungible Ducks are the first randomised, hard-cap project on the Zilliqa blockchain.",
            "attributes": 
            [ 
                {
                    "display_type" : "string",
                    "trait_type": "Base", 
                    "value": base
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Beak", 
                    "value": beak
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
                    "value": oldAttributes["duck_base_occurrence_chance"]
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Beak Rarity", 
                    "value": oldAttributes["duck_beak_occurrence_chance"]
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Eyes Rarity", 
                    "value": oldAttributes["duck_eyes_occurrence_chance"]
                },
                {
                    "display_type" : "string",
                    "trait_type": "Hat Rarity", 
                    "value": oldAttributes["duck_hats_occurrence_chance"]
                },
                {
                    "display_type" : "string",
                    "trait_type": "Outfit Rarity", 
                    "value": oldAttributes["duck_outfit_occurrence_chance"]
                },

                
            ],
            "transparent": "ipfs://" + ipfshash,
            "quick_resource": "https://nfds.s3.eu-west-2.amazonaws.com/DUCK_" + str("{0:0=4d}".format(id)) + ".png"
        }
        json.dump(result, write_file)

    return



for id in range(1, 1 + 2):
    print("Gen duck " + str(id))
    genNewMeta(id)
