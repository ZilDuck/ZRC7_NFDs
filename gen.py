import glob
import numpy as np
from PIL import Image, ImageColor
from random import randrange
import json

currentURIs = []

#teal
#[199, 255, 233]
backgroundColours = ["#9EC8FF", "#D091FF","#EB6C6C", "#C7FFE9", "#FFA491", "#CEFF9E", "#F7BAFF", "#FFA97A"]

for filename in glob.glob('./hashes/*.png'):
    currentURIs.append(filename)

def getColour ():
    number = randrange(0, 8)
    color = backgroundColours[number]
    print("Chose colour " + str(color) + " with number " + str(number))
    return color

def filterList(key, value) :
    print (key)
    print (value)
    file = "./currentducks.json"
    with open(file) as json_file:
        data = json.load(json_file)
        result = []
        for p in data:
            if value.lower() in p[key].lower() :
                result.append(p)

        return result

def getIDFromHash (originalHash):
    result = filterList("image", value="https://gateway.pinata.cloud/ipfs/"+originalHash)[0]
    print("Get id from hash: " + result["id"])
    return result["id"]

def saveJSON (originalHash):
    currentduck = filterList(key="image", value="https://gateway.pinata.cloud/ipfs/"+originalHash)[0]

    metadataLink = currentduck['metadata']
    id = currentduck['id']

    metadataHash = metadataLink.split('https://gateway.pinata.cloud/ipfs/')[1]
    metadataFile = './metadata/REGEN_' + metadataHash + '.json'

    with open(metadataFile) as oldMetadata:
        data = json.load(oldMetadata)
        print(data)

    with open(location, "w") as write_file:
        result = {        
            "name": "Cloud Quackers",
            "description": "Non-Fungible Ducks",
            "resource": "", #arweave coloured
            "resource_mimetype": "image/png",
            "external_url": "https://duck.community",
            "external_description": "Non-Fungible Ducks are the first randomised, hard-cap project on the Zilliqa blockchain.",
            "attributes": 
            [ 
                {
                    "display_type" : "string",
                    "trait_type": "Base", 
                    "value": "Mandarin Shiny"
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Base", 
                    "value": "10%"
                }, 
                {
                    "display_type" : "string",
                    "trait_type": "Base occurance chance", 
                    "value": "0.91%"
                },


            ],
            "transparent": "ipfs://" + originalHash,
            "quick_resource": "s3"
        }
        json.dump(result, write_file)
    return

def genNewDuck (filename):
    hash = filename.split('./hashes/DUCK_')[1].split('.png')[0]
    print("Hash: " + hash)
    oldImg =Image.open(filename)
    array = np.zeros([2000, 2000, 3],dtype=np.uint8)
    array[:,:] = ImageColor.getcolor(getColour(),"RGB")
    background = Image.fromarray(array)

    background.paste(oldImg, (0,0), oldImg)    

    print("Get id from duck with old hash: " + hash)
    id = getIDFromHash(hash)

    jpg_file = "./generated/coloured_" + id + "_" + hash + ".png"
    background.save(jpg_file)

    

    return

i = 0
for filename in currentURIs:
    print("\n\nGenerating duck " + filename)
    
    genNewDuck(filename)
    i+=1
    
    if i > 10:
        break
    