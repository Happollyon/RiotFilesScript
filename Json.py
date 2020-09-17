import sys
import json
from os.path import isfile
import os

jsonPath= sys.argv[1]
imageFolder =  sys.argv[2]


with open(jsonPath,encoding="utf8") as jsonFile:
     data = json.load(jsonFile)
     
for filename in os.listdir(imageFolder):
    name = filename.split('.')[0]
    championData = data['data'][name]
    os.rename(os.path.join(imageFolder, filename), os.path.join(imageFolder, filename.replace(name, championData['key'])))
    
       
         #championData = data['data'][champion]
         #print(championData['key'])




#For each image in folder
    #find a matching key in json And rename file to keyValue
    #if no key is found return
