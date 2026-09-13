import re
fname = input("Enter file: ")
fh = open(fname)
total = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total += int(number)
print(total)