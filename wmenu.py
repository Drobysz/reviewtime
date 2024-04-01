import os
import wfuncs
import time as t

funcslib = {'cr' : wfuncs.create, 'rm' : wfuncs.remove, 'crw' : wfuncs.create_wordblocks, 'shed' : wfuncs.shedule,'rn' : wfuncs.rename }
combar = ''

while combar != exit :
    input('-Press Enter to continue- ')
    print('*-------Word Timer-------*\n')
    #menu
    for dpath, dname, files in os.walk('languages'):
        
        if dpath.count('/') > 0 :
            #directory name
           print('--' * dpath.count('/')+'>'+os.path.basename(dpath))
           #file names
           
           for item in files :
                
                if item == '.DS_Store' : os.remove(dpath+'/'+item)
                else : print('  ' * dpath.count('/')+' * '+item)
                                         
    print('\n*========================*')  

    #command bar implementation    
        
    combar = input('Input a command : ')
    command = combar[ 1 : combar.index(' ') ]
    info = combar[ combar.index(' ')+1 : len(combar) ]

    #command launch

    if command in funcslib.keys() : funcslib[command](info)
    else : print('\nWrong command!\n')
    



    
    
     
  