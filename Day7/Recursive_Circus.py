from copy import deepcopy


file = open("input.txt")

rows = {}
rows_higher = []
lines = file.readlines()
for index, line in enumerate(lines):
    if len(line.split()) == 2:
        rows[line.split()[0]] = None
    else:
        a = []
        for item in line.split()[3:]:
            if item[-1] == ",":
                item = item[:-1]
            a.append(item)

        rows[line.split()[0]] = [elem for elem in a]

values = []
for v in rows.values():
    if v is not None:
        for item in v:
            values.append(item)

for k in rows.keys():
    if k not in values:
        print(k)
        