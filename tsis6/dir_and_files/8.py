#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists(r'/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/todelete.txt'):
    os.remove(r'/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/todelete.txt')
else:
    print("The file does not exist")