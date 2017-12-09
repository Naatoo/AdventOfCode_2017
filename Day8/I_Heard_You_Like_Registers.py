file = open("input.txt")
lines = file.readlines()

registers = {}
for row in lines:
    line = row.split()
    if line[0] not in registers:
        registers[line[0]] = 0

register_max = 0
for line in lines:
    row = line.split()
    num = registers[row[4]]

    string = str(num) + row[5] + row[6]

    if eval(string):
        registers[row[0]] = registers[row[0]] + int(row[2]) if row[1] == "inc" else registers[row[0]] - int(row[2])

    if registers[row[0]] > register_max:
        register_max = registers[row[0]]

print("Part 1:", max([v for v in registers.values()]))
print("Part 2:", register_max)
