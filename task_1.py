import os
from pathlib import Path
import random, string


path=input("Enter a full directory path : ")

if os.path.exists(path):
    for count, filename in enumerate(os.listdir(path)):
        print(filename)
        filename1, file_extension = os.path.splitext(filename)
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        os.rename( path+"/"+filename,path+'/New__'+filename1+'__'+x+file_extension)
        print("File name changed  Successfully")
else:
    print("Directory Path Doesnt exist")