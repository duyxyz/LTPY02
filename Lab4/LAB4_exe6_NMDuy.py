#Exercise 6
#Redo the previous exercise with the following differences:
#now the user input strings (maybe representing numbers but not necessarily)
#now the user input the strings all at once in the form of a string, each string separated by exactly one space character.
#Nguyễn Minh Duy
#05/03/2026

chuoi = input("nhap cac chuoi cach nhau bang mot dau cach: ").strip()

phan = chuoi.split(" ")

tui = []

for p in phan:
    if p not in tui:
        tui.append(p)

print("tui cua ban:", tui)






