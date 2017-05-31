# Write a java program that prints
# the following sequences of values using loops
# 18, 27, 36, 45, 54, 63

start = 18
end = 63
numberlist = [start]  # to store the number
i = 0
while (True):
    start = start + 9  # pattern of the series
    numberlist.append(start)
    if start == end:  # breaking out of loop when end is found
        break

print(numberlist)
