#Write a Python program to count the number of lines in a text file.
import os

path = r'/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/demofile.txt'

file = open(path, 'rt')

cnt = 0
while file.readline():
    cnt += 1

print(cnt)