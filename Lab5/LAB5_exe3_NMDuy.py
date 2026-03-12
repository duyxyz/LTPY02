#Lab5
#Exercise 3
#Redo exercise 1 but now, apart from the count and the average, 
#the Python script should also compute the minimum and the maximum values from the file. 
#For this exercise, you're required to use only the while loop construct (no for loop). 
#These are two sample logs of the execution of the program  (user input is in bold and underlined):
#Nguyễn Minh Duy
#12/03/2026



filepath = input("nhap duong dan tep: ")

with open(filepath) as f:
    tong = 0
    dem = 0
    nho_nhat = None
    lon_nhat = None

    dong = f.readline()
    while dong != "":
        so = int(dong)
        tong += so
        dem += 1
    if nho_nhat is None or so < nho_nhat:
            nho_nhat = so
    if lon_nhat is None or so > lon_nhat:
            lon_nhat = so

    dong = f.readline()

trung_binh = round(tong / dem, 2)
print(f"gia tri nho nhat la {nho_nhat}")
print(f"gia tri lon nhat la {lon_nhat}")
print(f"gia tri trung binh la {trung_binh}")