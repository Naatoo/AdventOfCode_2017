file = open("input.txt")
txt = file.read().strip()
txt_table = txt.split(",")

sw = txt_table.count("sw") - txt_table.count("ne")
nw = txt_table.count("nw") - txt_table.count("se")
s = txt_table.count("s") - txt_table.count("n")
sw += nw
s -= nw

print("Part 1:", sw + s)
