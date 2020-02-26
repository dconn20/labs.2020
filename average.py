# This program reads in numbers until
# the user enters 0
# it will them print back out again
# and their average

numbers = []

number = int (input ("Enter number(0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter another(0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))