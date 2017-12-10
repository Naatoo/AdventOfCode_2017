file = open("input.txt")
inp = file.read()
inplist = list(inp)

cur = 0
while True:
    try:
        if inplist[cur] == "!":
            inplist.pop(cur)
            inplist.pop(cur)
            cur = 0
        cur += 1
    except IndexError:
        break
inplist.pop()

cur = 0
find_end = 0
find_start = 1
garbage = 0
while True:
    try:
        if find_start == 1:
            if inplist[cur] == "<":
                id_start = cur
                find_end = 1
                find_start = 0
        if find_end == 1:
            if inplist[cur] == ">":
                garbage += len(inplist[id_start + 1:cur])
                del(inplist[id_start:cur + 1])
                cur = 0
                find_start = 1
                find_end = 0
        cur += 1
    except IndexError:
        break

flist = list(filter(lambda x: x != ",", inplist))
level = 0
score = 0
for char in flist:
    if char == '{':
         score += 1 + level
         level += 1
    elif char == '}':
         level -= 1

print("Part 1:", score)
print("Part 2:", garbage)
