from copy import deepcopy


file = open("input.txt")
line = file.read()
banks = list(map(int, line.strip().split("\t")))

i = 0
sets = []

while True:
    i += 1
    for index, bank in enumerate(banks):
        if bank == max(banks):
            maximum_id = index
            maximum_value = bank
            break
    banks[maximum_id] = 0
    for number in range(1, maximum_value + 1):
        try:
            banks[maximum_id + number] += 1
        except IndexError:
            maximum_id = - number
            banks[maximum_id + number] += 1

    if banks in sets:
        for index, set_now in enumerate(sets):
            if set_now == banks:
                print("Part 1:", i)
                print("Part 2:", len(sets) - index)
        break
    else:
        sets.append(deepcopy(banks))
