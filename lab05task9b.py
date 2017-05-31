# Write a java program that prints
# the following sequences of values using loops
# -10, -5, 0, 5, 10, 15, 20

start = -10
end = 20
numberlist = [start]  # to store the number
i = 0
while (True):
    start = start + 5  # pattern of the series
    numberlist.append(start)
    if start == end:  # breaking out of loop when end is found
        break

print(numberlist)
