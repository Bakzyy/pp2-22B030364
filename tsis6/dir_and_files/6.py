#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

prefix_path = r'/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/files'
path = "{}/{}.txt"

for i in range(65, 91):
    
    dir_path = path.format(prefix_path, chr(i))
    
    if os.path.exists(dir_path):
        os.remove(dir_path)
    
    file = open(dir_path, 'x')
    
