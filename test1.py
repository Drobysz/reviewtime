import os

for dpath,dname,file in os.walk('languages'):

    if file == '.DS_Store' : os.remove(dpath+'/'+file)
    if 
    