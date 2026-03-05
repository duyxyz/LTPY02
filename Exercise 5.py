#Exercise 5
#Write a script which reads 5 distinct integers step by step from the user and print them out in a list. 
#If the user input a number previously selected, the new integer is not added in the list and the script print a message to notify the user that the number was already selected.
bag = []

while len(bag) < 5:
    number = int(input("Enter a number: "))

    if number in bag:
        print(number, "is already in the bag")
    else:
        bag.append(number)

print("Your bag:", bag)