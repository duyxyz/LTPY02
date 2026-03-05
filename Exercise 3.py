#Exercise 3
#Write a Python program to convert a temperature in degree Celsius into the same temperature in Fahrenheit and vice-versa.
#The initial scale used is given by the user when she/he inputs the temperature to convert. 
#These are sample logs of the execution of the program  (user input is in bold and underlined):
#Nguyễn Minh Duy
#05/03/2026

nhiet_do = input("nhap nhiet do: ")

phan = nhiet_do.split("°")

if len(phan) != 2:
    print("khong biet don vi")
else:
    so = phan[0]
    don_vi = phan[1]

    if don_vi == "C":
        c = float(so)
        f = c * 9/5 + 32
        print(so + "°C = {:.2f}°F".format(f))

    elif don_vi == "F":
        f = float(so)
        c = (f - 32) * 5/9
        print(so + "°F = {:.2f}°C".format(c))

    else:
        print("khong biet don vi")

















