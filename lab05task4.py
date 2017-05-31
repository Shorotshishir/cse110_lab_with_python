# Write a program that prints the first ten even positive integers

i = 10 # how many numbers u want to print
number = 1
numberlist=[]

while (True):
    if number % 2 == 0:
        numberlist.append(number)
    number+=1
    if len(numberlist) == i:
        break

print(numberlist)