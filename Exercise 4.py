#Exercise 4
#Write a Python program to compute the yearly score and the rating of a student. 
#The user inputs the score of each quarters (three float numbers on the same line spearated by exactly one space) then the program computes and displays the average and the corresponding rating. The following table defines how to compute the rating
#Nguyễn Minh Duy
#29/01/2026

score = input("enter your quarter scores: ")

parts = score.split(" ")

if len(parts) != 3:
    print("vui long nhap lai")
else:
    s1 = float(parts[0])
    s2 = float(parts[1])
    s3 = float(parts[2])

    average = (s1 + s2 + s3) / 3

    print("your final score is {:.2f}".format(average))

    if average < 4:
        print("rating: very poor")
    elif average < 5.5:
        print("rating: poor")
    elif average < 7:
        print("rating: fair")
    elif average < 8.5:
        print("rating: good")
    elif average < 9.5:
        print("rating: very good")
    else:
        print("rating: outstanding")