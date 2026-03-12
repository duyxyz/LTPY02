#Lab5
#Exercise 2
#Write a Python program to read a file which content is the description of some Marvel characters and to write a file with the same content but with a different layout. The file avengers.txt, an example of the input file (provided) have the following structure:
#each character is described using exactly three lines:
#the first line is the name of the character (like Tony Stark)
#the second line is the nickname of the character (like IronMan)
#the third line is the name of the actor playing that character 
#the file has a number of lines multiple of three
#Nguyễn Minh Duy
#12/03/2026

input_path = input("Duong dan tep dau vao: ")
output_path = input("Duong dan tep dau ra: ")

with open(input_path) as inp, open(output_path, "w") as out:
    lines = inp.readlines()
    i = 0
    while i < len(lines):
        Name = lines[i].strip()
        Nickname = lines[i + 1].strip()
        Actor = lines[i + 2].strip()

        out.write(f"Name: {Name}\n")
        out.write(f"Nickname: {Nickname}\n")
        out.write(f"Actor: {Actor}\n")

        i += 3

print("Hoan tat.")






