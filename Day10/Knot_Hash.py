file = open("input.txt")
numbers = file.read().strip()
lengths_temp = numbers.split(",")
lengths = list(map(int, lengths_temp))

num_list = []
[num_list.append(x) for x in range(255)]
num_list = [0, 1, 2, 3, 4]
lengths = [3, 4, 1, 5]
skip = 0
pos = 0
for length in lengths:
    if length + pos < 5:
        list_temp = num_list[pos:length]
        print(list_temp)
        for index, place in enumerate(list_temp):
            num_list[pos + length - index - 1] = place
    else:
        list_temp = num_list[pos:]
        rest = 4 - pos

        [list_temp.append(x) for x in num_list[:rest - 1]]

        list_temp_reversed = list_temp.reverse()

        print(list_temp_reversed)
        for index, number in enumerate(list_temp_reversed[len(num_list[pos:]) + 1:]):
            print(index + pos)
            num_list[pos + index] = number

    print("Full", num_list)

    pos += length + skip
    skip += 1
