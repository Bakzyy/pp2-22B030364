#Write a Python program to copy the contents of a file to another file
import os 
init_file = open('/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/demofile.txt', 'r')

init_read = init_file.read()

init_file.close()

final_file = open('/Users/bakustar2005/Documents/pp2/tsis6/dir_and_files/test.txt', 'w')

final_file.write(init_read)

final_file.close()
