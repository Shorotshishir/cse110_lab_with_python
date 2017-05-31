# Write a java program that prints
# the following sequences of values using loops
# 24, 18, 12, 6, 0, -6

start = 24
end = -6
numberlist = [start]  # to store the number
i = 0
while (True):
    start = start - 6  # pattern of the series
    numberlist.append(start)
    if start == end:  # breaking out of loop when end is found
        break

print(numberlist)
