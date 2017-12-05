from copy import deepcopy
file = open("data.txt", "r")

lines = file.readlines()
lines.pop(-1)
numbers = []

for line in lines:
    line = line.strip()
    numbers.append(int(line))

numbers_p2 = deepcopy(numbers)

cur = 0
no = 0

while True:
    try:
        temp = cur
        cur += numbers[cur]
        numbers[temp] += 1
        no += 1
    except IndexError:
        break

print(no)

# ---------- PART 2 ----------

cur = 0
no = 0
while True:
    try:
        temp = cur
        cur += numbers_p2[cur]
        if cur - temp >= 3:
            numbers_p2[temp] -= 1
        else:
            numbers_p2[temp] += 1
        no += 1
    except IndexError:
        break

print(no)
