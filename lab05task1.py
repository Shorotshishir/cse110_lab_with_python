# Write a program that reads five numbers as input from the user, and prints whether the numbers are odd
#  or even.


i = 0  # integer for iteration
numberlist = []  # list to store the numbers
print('you need to input 5 numbers')

while len(numberlist) < 5:
    print('please enter a number : ')
    numberlist.append(input())
    print('numbers left to input : ' + str(5 - len(numberlist)))

# checking odd even
for number in numberlist:
    if int(number) % 2 == 0:
        print(number + ' is an even number')
    else:
        print(number + ' is a odd number')
