'''
this script takes files store in 'base_files' directory and copies then to the 'move_file' directory
in the process it also changes the naming convention to omit anything before the second underscore
meaning Row_xxx_XXXXX_authtype in 'base_files' is moved as XXXXX_authtype in 'move_files'

last update: 2020.11.20 by JL
'''

import os
import shutil

#set base and move directories
basedir = r'C:\Users\jleyv\PycharmProjects\FileNameEdit\base_files'
movedir = r'C:\Users\jleyv\PycharmProjects\FileNameEdit\move_files'

#create list of items per directory and count items
baselist = os.listdir(basedir)
basecount = len(baselist)

movelist = os.listdir(movedir)
movecount = len(movelist)

#print count
print('count before execution:')
print('there is currently', basecount, 'files in the base directory')
print('there is currently', movecount, 'files in the move directory')

#copy each file from base dfirectory to move directory with new name
for i in baselist:
    basefile = r'C:\Users\jleyv\PycharmProjects\FileNameEdit\base_files\\'+ str(i)   #read name of independent file
    groups = i.split("_")    #split name by '_'
    _ = '_'.join(groups[:2]), '_'.join(groups[2:])   #group items above by 'before the second '_' and after the second '_'
    rename = _[1]   #select item that corresponds to after second '_' as new name
    copyfile = r'C:\Users\jleyv\PycharmProjects\FileNameEdit\move_files\\' + str(rename)    #provide path to copy to including new name

    shutil.copy(basefile, copyfile) #copy file

#new count
movelist = os.listdir(movedir)
movecount = len(movelist)

#print recount
print('\n')
print('count after execution:')
print('there is currently', basecount, 'files in the base directory')
print('there is currently', movecount, 'files in the move directory')