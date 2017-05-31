# Write a  program which adds all numbers that
# are multiples of both 7 and 9 up to 600.

end = 600
start = 0
total = 0

for i in range(0, 600):
    if (i % 7) & (i % 9):
        total = total + i

print(total)
