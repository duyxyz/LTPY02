#Exercise 4
#Write a Python program to compute the yearly score and the rating of a student. 
#The user inputs the score of each quarters (three float numbers on the same line spearated by exactly one space) then the program computes and displays the average and the corresponding rating. The following table defines how to compute the rating
#Nguyễn Minh Duy
#05/03/2026

diem = input("nhap diem 3 hoc ky: ")

phan = diem.split(" ")

if len(phan) != 3:
    print("vui long nhap lai")
else:
    d1 = float(phan[0])
    d2 = float(phan[1])
    d3 = float(phan[2])

    trung_binh = (d1 + d2 + d3) / 3

    print("diem trung binh la {:.2f}".format(trung_binh))

    if trung_binh < 4:
        print("xep loai: rat kem")
    elif trung_binh < 5.5:
        print("xep loai: kem")
    elif trung_binh < 7:
        print("xep loai: trung binh")
    elif trung_binh < 8.5:
        print("xep loai: kha")
    elif trung_binh < 9.5:
        print("xep loai: gioi")
    else:
        print("xep loai: xuat sac")




















