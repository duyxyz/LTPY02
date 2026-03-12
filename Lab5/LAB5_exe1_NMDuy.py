#Lab 5
#Exercise 1
#Write a Python program to ask the user for an input text file, then to read each integer from that text file and finally to print the total number of integers and the average value of those integers. 
#The text file must contain only integers as one integer per line. Two such files are provided: the user that the number was already selected.
#Nguyễn Minh Duy
#12/03/2026

filepath = input("Nhap duong dan tep: ")
soluong = 0
trungbinh = 0 
with open(filepath) as f:
    for line in f:
        soluong += int(line)
        trungbinh += 1
 
average = round(soluong / trungbinh, 2)
print(f"Số lượng: {soluong}, trung bình: {trungbinh}")
 



