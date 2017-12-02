file = open("data.txt")
lines = file.readlines()

diff_sum = 0
for line in lines[:-1]:
    cur_line = list(map(int, line.split()))
    diff_sum += max(cur_line) - min(cur_line)

print(diff_sum)

# ---------- PART 2 ----------

div_sum = 0
for line in lines[:-1]:
    cur_line = list(map(int, line.split()))
    for number in cur_line:
        for n in cur_line:
            if number % n == 0 and number != n:
                div_sum += number // n

print(div_sum)
