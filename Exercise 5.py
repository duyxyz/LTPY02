#Exercise 5
#Write a script which reads 5 distinct integers step by step from the user and print them out in a list. 
#If the user input a number previously selected, the new integer is not added in the list and the script print a message to notify the user that the number was already selected.
#Nguyễn Minh Duy
#05/03/2026

tui = []

while len(tui) < 5:
    so = int(input("nhap mot so: "))

    if so in tui:
        print(so, "da co trong tui")
    else:
        tui.append(so)

print("tui cua ban:", tui)