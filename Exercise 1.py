#Lab 4
#Exercise 1
#Write a Python program to extract the filename and the folder information from a Windows filepath. For example, for the filepath
#C:\Program\Python\lab2\test.py
#the filename is test.py and the folder information is C:\Program\Python\lab2. 
#This is a sample log of the execution of the program (user input is in bold and underlined)
#Nguyễn Minh Duy
#29/01/2026

path = input("file path: ")
parts = path.split("\\")
filename = parts[-1]
folder = "\\".join(parts[:-1])
print(filename)
print(folder)

