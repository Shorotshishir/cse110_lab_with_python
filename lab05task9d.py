
# Write a program that prints
# the following sequences of values using loops
# 2, -4, 6, -8, 10, -12

start = 2
end = -12
numberlist = []  # to store the number
i = 1
sign = 1
while (True):
    start = i*sign*(2)  # pattern of the series
    numberlist.append(start)
    sign = sign*(-1)
    i+=1
    if start == end:  # breaking out of loop when end is found
        break

print(numberlist)
