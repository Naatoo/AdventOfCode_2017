file = open("data.txt")

not_valid = 0
id = 0

for line in file.readlines():
    not_valid_line = 0
    exp_list = tuple(line.split())
    for exp in exp_list:
        temp_list = list(exp_list)
        temp_list.remove(exp)
        if exp in temp_list:
            not_valid_line = 1
    if not_valid_line == 1:
        not_valid += 1
    id += 1

valid = id - not_valid - 1
print(valid)
file.close()

# ---------- PART 2 ----------

file = open("data.txt")

valid = 0
for line in file.readlines():
    exp_list = line.split()
    sorted_list = []
    for exp in exp_list:
        sorted_list.append(''.join(sorted(exp)))
    if len(set(sorted_list)) == len(exp_list):
        valid +=1

print(valid - 1)
file.close()
