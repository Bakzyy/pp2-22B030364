#Write a Python program to write a list to a file.
import os

path = r'/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/test.txt'

file = open(path, 'wt')

list = ["Write ", "a ", "Python ", "program ", "to ", "write ", "a ", "list ", "to ", "a ", "file."]

for i in list:
    file.write(i)