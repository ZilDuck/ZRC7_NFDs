import glob
import numpy as np
from PIL import Image, ImageColor
from random import randrange
import json
import imagehash

currentURIs = []

for filename in glob.glob('./generated/generated/*.png'):
    currentURIs.append(filename)

currentURIs.sort()

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

def addIDToColourJSON (id, hash):
    with open("./compressedHashes.json", "r+") as file:
        fileData = json.load(file)
        
        newDuck = {
            "id": id,
            "hex": hash,
        }
         
        fileData["ducks"].append(newDuck)
        file.seek(0)
        json.dump(fileData, file, indent=4)
    return

def genNewDuck (duck):
    print(duck)

    oldImg =Image.open(duck)
 
    #create 800px compressed for s3
    quick = oldImg.resize((800,800),Image.ANTIALIAS)
  
    hash = imagehash.phash(quick)
    print(str(hash) + "\n")
    fileName = duck.split(".png")[0] + "_" + str(hash) + ".png" 
    fileName = fileName.replace("./generated/generated/", "./generated/compressed/")
    print(fileName)
    quick.save(fileName, "PNG", optimize=True, quality=20)

    id = duck.split("d/generated/")[1].split(".png")[0]

    return


for duck in currentURIs:
        print("Gen duck " + str(duck))
        genNewDuck(duck)
    
