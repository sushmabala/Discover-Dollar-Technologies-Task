import os
path=input("Enter a Directory path : ")
filename = input("Enter a File name you want to search for : ")
print("Searching...")
for root, dirs, files in os.walk(path):  
    if filename in files:
        a=True
        break
    else:
        a=False

if(a):
    print("\nFile Found")
else:
    print("\nFile not Found")