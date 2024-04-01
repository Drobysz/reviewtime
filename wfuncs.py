import os  
import shutil
import time as t

wr = {'r':'rules','w' : 'words'}
timer = [1,3,7,27,90,0]

def create(lan):

    lancount = tuple(lan).count(' ')
    #creating a new language library /cr language
    if lancount == 0 :
        os.makedirs('languages/'+lan+'/'+wr['w'])
        os.makedirs('languages/'+lan+'/'+wr['r'])
        shutil.copytree('languages/'+lan, 'trashbin/deleted_'+lan)
    #adding a new book(a txt file) /cr language w/r(words/rules) a book name
    elif lancount == 2:
        lanindex = tuple(lan).index(' ')
        path = 'languages/'+lan[ 0 : lanindex ] + '/' + wr[ lan[lanindex + 1] ] + '/' + lan[lanindex + 3 : len(lan)]+'.txt'
        with open(path ,'w') as fp: fp.write('')
                  

def remove(lan):
    lancount= tuple(lan).count(' ')

    if lancount == 2:
        lanindex = tuple(lan).index(' ')
        path = 'languages/'+lan[ 0 : lanindex ] + '/' + wr[ lan[lanindex + 1] ] + '/' + lan[lanindex + 3 : len(lan)]+'.txt'
        os.remove(path)

def create_wordblocks(info):

    for dpath, dname, files in os.walk('languages'):
        for file in files:
            if file == info+'.txt':
                with open(dpath+'/'+file, 'a') as fp:
                   for i in input('Write word block names (name1 name2 name3 ...) : ').split(): fp.write(i+':'+str(t.time())+'\n')


def shedule(gap):
    
    weeklib = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    day = 86400
    today = int( t.time() )
    for i in range(1):
        print('----------',i + 1,'----------')
        for i in range(7):

           print('\n       '+t.strftime('%a', t.gmtime( today ) )+'       ')

           for dpath, dname, files in os.walk('languages'):
              if dpath.count('/') == 1 : print('->'+ dpath[ dpath.index('/') + 1 : len(dpath) ] ) 
              for file in files:
                 if file[-4:] == '.txt' :
                   print( '   *' + file[0 : -4]+' : ',end='' )
                   with open(dpath+'/'+file,'r') as fp:

                       for wblock in fp.readlines():
                       
                         file_date = int( ( today - int( wblock[ wblock.index(':')+1 : wblock.index('.') ] ) ) / day )
                         for i in range(4):

                            if file_date == sum( timer[0:i+1] ) : print( wblock[ 0 : wblock.index(':') ], end=' ' )  

                 print()    

           today += day

def rename(info):
       
       for dpath, dname, files in os.walk('languages'):

           for file in files:

               if file == info + '.txt' : os.rename(dpath + '/' + file.dpath + '/' + input('Input a new name : ') + '.txt')

           for name in dname:
              
               if ( name == info ) and ( ( name != 'rules' ) and ( name != 'words' ) ) : os.rename(dpath + '/' + name,dpath + '/' + input('Input a new name : '))







        
