import os  
import email
from emaildata.metadata import MetaData

path=input("Enter the Directory path :")
filename = input("Enter the file name :")
message = email.message_from_file(open(path+"/"+filename))
filename1, file_extension = os.path.splitext(filename)
html = Text.html(message)
myfile = open(filename1+".html", 'w')
myfile.write(html)
myfile.close()

