# file = open("input.txt").readlines()
from copy import deepcopy
layers = {}

i = 0
for line in open("input.txt"):
    values = line.split(": ")
    layers[int(line.split(": ")[0])] = [int(line.split(": ")[1].replace("\n", ""))]

for lay in range(85):
    if lay not in layers.keys():
        layers[lay] = None
    else:
        layers[lay].append(0)
        layers[lay].append(0)
print("start", layers)

layers2 = deepcopy(layers)
caugth = []

for index in range(len(layers)):
    try:
        if layers[index][2] == 0:
            caugth.append(index)
    except TypeError:
        pass
    for v in layers.values():
        if v is not None:
            if v[1] == 0 and v[2] < v[0]:
                v[2] += 1
                if v[0] - 1 == v[2]:
                    v[1] = 1
                continue
            if v[1] == 1 and v[2] > 0:
                v[2] -= 1
                if v[2] == 0:
                    v[1] = 0


print("Part 1:", sum([number * layers[number][0] for number in caugth]))



