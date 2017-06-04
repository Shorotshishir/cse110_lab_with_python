number = int(input('Enter a height '))

for i in range(1, number + 1):
    for k in range(number, i, -1):
        print(' ', end="")

    for j in range(i):
        print('*', end="")


    print('')