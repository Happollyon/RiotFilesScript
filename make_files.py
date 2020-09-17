from os import listdir, walk
from os.path import isfile,join
import os
#find each folder in assets
myPath='C:\\Users\\siber\Desktop\\DuoPointMobile\\assets'
list = [f.path for f in os.scandir(myPath) if f.is_dir()]

for intem in list:
    folderName= os.path.basename(intem)
    jsName=myPath+'\\'+os.path.basename(intem)+'.js'
    #create data to be appended 
    f = open(jsName,'a')
    append =  'const images_'+folderName+'={'
    f.write(append)
    #got to all files in that folder
    x = [f.name for f in os.scandir(intem) if f.is_file()]
    
    for y in x :
        append2 = y.split('.')[0]+': require(\'./'+folderName+'/'+y+'\'),\n'
        f.write(append2)
    
    f.write('}\n export default images_'+folderName)
    # create the string file 'name': require(./os.path.basename('intem'))+/'name'+'.png'
    print('Done!')
    #f = open(jsName,'a')

#create a js file with that folders name

