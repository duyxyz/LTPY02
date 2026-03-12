#Lab5
#Exercise 4
#Redo exercise 3, now using only the for loop and the string method readline at the same time (why do we need that?)
#Nguyễn Minh Duy
#12/03/2026
filepath = input("nhap duong dan tep: ")

with open(filepath) as f:
    tong = 0
    dem = 0
    nho_nhat = None
    lon_nhat = None

    for dong in f:
        so = int(dong)
        tong += so
        dem += 1

        # cap nhat gia tri nho nhat
        if nho_nhat is None or so < nho_nhat:
            nho_nhat = so

        # cap nhat gia tri lon nhat
        if lon_nhat is None or so > lon_nhat:
            lon_nhat = so

trung_binh = round(tong / dem, 2)
print(f"gia tri nho nhat la {nho_nhat}")
print(f"gia tri lon nhat la {lon_nhat}")
print(f"gia tri trung binh la {trung_binh}")