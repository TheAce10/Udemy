# Code to search for files with particular extensions and delete them
import os

x='C:/Users/hp'
print('\n\nWelcome to File Extinct')
print("Requirements:\n First lets navigate to targeted folder relative from \"C:/Users/hp\" or paste path seperated by forward slash /")
while x != "1":
    os.chdir(x)
    print("Current Folder Path: "+ os.getcwd() + "\nDirectories and desFiles In Current Folder")
    ls = os.listdir()
    for i in ls:
        print(i)
    
    x= input("If in targeted folder Enter 1\n")
print("We\'re in the targeted Folder, now enter file extension to view files for deletion e.g. (.py)")
ext = input()

print(os.getcwd())

s= os.listdir()
print(s)

f_del= []
for file1 in s:
    p = 0
    for n in file1:
        if n== '.':
            break
        p += 1
    f_ext= file1[p:len(file1)]
    if f_ext == ext:
        f_del.append(file1)
print(f_del)
for fname in f_del:
    print(f"file {fname} has been deleted")
    os.remove(file1)
print(os.listdir())
