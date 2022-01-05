import os,shutil 

src = input("Enter the location of the folder to be sorted : ") 

listOfFiles = os.listdir(src) 

for file in listOfFiles: 
    name,ext = os.path.splitext(file) 
    ext = ext[1:] 
    
    if ext == '': 
        continue 
        
    if os.path.exists(src+"/"+ext): 
        shutil.move(src+'/'+file,src+"/"+ext+'/'+file) 
    else: 
        os.makedirs(src+'/'+ext) 
        shutil.move(src+'/'+file,src+"/"+ext+'/'+file)    