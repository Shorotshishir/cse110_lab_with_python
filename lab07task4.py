height = int(input('Enter a height '))
width = int(input('Enter a width '))

for i in range(1, height + 1):
    for j in range(1, width + 1):
        print(j, end="")
    print('')
