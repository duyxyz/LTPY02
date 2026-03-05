#Exercise 2

#Write a Python program to compute the minimum and the maximum values from a sequence of integers. 
#The user should enter a string made of integer values separated by exactly one space. 
#This is a sample log of the execution of the program  (user input is in bold and underlined):
#Nguyễn Minh Duy
#05/03/2026

cac_so=input("nhap cac so:")
danh_sach_so=cac_so.split(" ")
danh_sach_so=[int(x) for x in danh_sach_so]
so_nho_nhat=min(danh_sach_so)
so_lon_nhat=max(danh_sach_so)
print("min =",so_nho_nhat,", max =",so_lon_nhat)




