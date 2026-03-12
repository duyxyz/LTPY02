#Exercise 7
#Write a script which reads integer numbers step by step from the user, until she/he enter 0 (to mean stop). 
#Then the script prints out the list of all even numbers entered and the list of all odd numbers entered.
#05/03/2026

so_chan = []
so_le = []

while True:
    so = int(input("nhap mot so: "))

    if so == 0:
        break

    if so % 2 == 0:
        so_chan.append(so)
    else:
        so_le.append(so)

print("cac so chan ban da nhap:", so_chan)
print("cac so le ban da nhap:", so_le)


























