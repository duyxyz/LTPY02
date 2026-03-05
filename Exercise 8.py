#Exercise 8
#Redo the previous exercise but now the user input the numbers all at once in the form of a string, each number separated by exactly one space character. Example:
#Enter numbers separated by exactly one space: 2 3 1 4 5 9 8 7
#The even numbers you entered: [2, 4, 8]
#The odd numbers you entered: [3, 1, 5, 9, 7]
#Nguyễn Minh Duy
#05/03/2026

chuoi = input("nhap cac so cach nhau bang mot dau cach: ").strip()

cac_so = chuoi.split(" ")

so_chan = []
so_le = []

for so in cac_so:
    n = int(so)

    if n % 2 == 0:
        so_chan.append(n)
    else:
        so_le.append(n)

print("cac so chan ban da nhap:", so_chan)
print("cac so le ban da nhap:", so_le)





