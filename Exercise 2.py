#Exercise 2

#Write a Python program to compute the minimum and the maximum values from a sequence of integers. 
#The user should enter a string made of integer values separated by exactly one space. 
#This is a sample log of the execution of the program  (user input is in bold and underlined):


numbers = input("your numbers: ")

num_list = numbers.split(" ")

num_list = [int(x) for x in num_list]

minimum = min(num_list)
maximum = max(num_list)

print("min =", minimum, ", max =", maximum)