# Write a program that reads five numbers from the user, and prints their average.


numberOfInput = 5  # specified ,

# if user chooses to restrict user input for himself
# numberOfInput = input('how many numbers u wan to input: ')

numberlist = []  # list to store the numbers

print('you need to input ' + numberOfInput + ' numbers')

# taking input
while len(numberlist) < 5:
    print('please enter a number : ')
    numberlist.append(input())
    # to print how many input is taken ,
    # print('numbers left to input : ' + str(numberOfInput - len(numberlist)))

# making average
sum = 0
for number in numberlist:
    sum = sum + int(number)

average = sum / len(numberlist)
print(average)
