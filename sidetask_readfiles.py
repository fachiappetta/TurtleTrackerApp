# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:52:57 2021

@author: fac16
"""

	### SIDE TASK
#read in the file
fileObj = open('./data/raw/sara.txt','r')

#read and print a single line
print(fileObj.readline())

#strong contents of a single line as a variable
lineString = fileObj.readline()
print(lineString)

#read entire contents of a text file
print(fileObj.readlines())

#print the last itme in this list
lineList = fileObj.readlines() 
print(lineList[-1])

#close the file
fileObj.close()

#writing text file
newFile = open('newfile.txt', 'w')

#write to new file
newFile.write("Hello world\nIt's me")

#close new file
newFile.close()

open('newfile.txt','a').write("\nSee what I did here")