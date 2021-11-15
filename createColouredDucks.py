import glob
import numpy as np
from PIL import Image, ImageColor
from random import randrange
import json

currentURIs = []

#teal
#[199, 255, 233]
backgroundColours = [
                    ["#82D5F5", "Blue"], 
                    ["#D091FF", "Lilac"],
                    ["#EB6C6C", "Peach"],
                    ["#C7FFE9", "Teal"],
                    ["#FFA491", "Beige"],
                    ["#CEFF9E", "Lime"],
                    ["#F7BAFF", "Pink"],
                    ["#FFA97A", "Orange"]]

for filename in glob.glob('./allDucks/*.png'):
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

def saveJSON (id):
    filePathOfOldJSON = `./metadata/DUCK_${String(i).padStart(4, '0')}.json`

    currentduck = filterList(key="id", value=id)[0]

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

def addIDToColourJSON (id, colourArray):
    with open("./regencolours.json", "r+") as file:
        fileData = json.load(file)
        
        newDuck = {
            "id": id,
            "hex": colourArray[0],
            "colour": colourArray[1]
        }
         
        fileData["ducks"].append(newDuck)
        file.seek(0)
        json.dump(fileData, file, indent=4)
    return

def genNewDuck (id):
    filename = "./allDucks/REGEN_" + str("{0:0=4d}".format(id)) + ".png"
    print(filename)

    colour = getColour()
    
    if (id == 8):
        colour = backgroundColours[1]

    oldImg =Image.open(filename)
    array = np.zeros([2000, 2000, 3],dtype=np.uint8)
    array[:,:] = ImageColor.getcolor(colour[0],"RGB")
    background = Image.fromarray(array)

    background.paste(oldImg, (0,0), oldImg)    


    jpg_file = "./generated/REGEN_" + str("{0:0=4d}".format(id)) + ".png"
    background.save(jpg_file)
    addIDToColourJSON(id, colour)
    return

for i in range(1, 1 + 8192):
    print("Gen duck " + str(i))
    
