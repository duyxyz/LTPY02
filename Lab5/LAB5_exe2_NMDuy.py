#Exercise 2
#Write a Python program to read a file which content is the description of some Marvel characters and to write a file with the same content but with a different layout. The file avengers.txt, an example of the input file (provided) have the following structure:
#each character is described using exactly three lines:
#the first line is the name of the character (like Tony Stark)
#the second line is the nickname of the character (like IronMan)
#the third line is the name of the actor playing that character 
#the file has a number of lines multiple of three
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