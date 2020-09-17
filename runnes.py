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
    print(name)    
    for a in range(5):
        print('a= '+str(a))
        for b in range(4):
            print('b= '+str(b))
            for c in range(4):
                print('c= '+ str(c))
                if c < len(data[a]['slots'][b]['runes']):
                    print(data[a]['slots'][b]['runes'][c]['key'])
                    if name == data[a]['slots'][b]['runes'][c]['key']:
                        print('updated')
                        championData = data[a]['slots'][b]['runes'][c]['id']
                        os.rename(os.path.join(imageFolder, filename), os.path.join(imageFolder, filename.replace(name, str(championData))))
                    
                    else:
                     
                        continue
                else:
                    continue





