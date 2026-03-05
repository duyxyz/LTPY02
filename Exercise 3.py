#Exercise 3
#Write a Python program to convert a temperature in degree Celsius into the same temperature in Fahrenheit and vice-versa.
#The initial scale used is given by the user when she/he inputs the temperature to convert. 
#These are sample logs of the execution of the program  (user input is in bold and underlined):
#Nguyễn Minh Duy
#29/01/2026



temp = input("enter your temperature: ")
parts = temp.split("°")
if len(parts) != 2:
    print("unknown scale")
else:
    number = parts[0]
    scale = parts[1]

    if scale == "C":
        c = float(number)
        f = c * 9/5 + 32
        print(number + "°C = {:.2f}°F".format(f))

    elif scale == "F":
        f = float(number)
        c = (f - 32) * 5/9
        print(number + "°F = {:.2f}°C".format(c))

    else:
        print("unknown scale")