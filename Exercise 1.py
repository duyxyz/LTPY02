#Lab 4
#Exercise 1
#Write a Python program to extract the filename and the folder information from a Windows filepath. For example, for the filepath
#C:\Program\Python\lab2\test.py
#the filename is test.py and the folder information is C:\Program\Python\lab2. 
#This is a sample log of the execution of the program (user input is in bold and underlined)
#Nguyễn Minh Duy
#05/03/2026

duongdan = input("duong dan file: ")
phan = duongdan.split("\\")
ten_file = phan[-1]
thu_muc = "\\".join(phan[:-1])
print(ten_file)
print(thu_muc)