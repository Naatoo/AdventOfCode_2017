file = open("data.txt")
number = file.read().strip()
file.close()

sum_digits_1 = 0
for n, digit in enumerate(number[:-1]):
    if digit == number[n+1]:
        sum_digits_1 += int(digit)

if number[-1] == number[0]:
    sum_digits_1 += int(number[-1])

print(sum_digits_1)


sum_digits_2 = 0
half_len = int(len(number) / 2)

for n, digit in enumerate(number[:half_len]):
    if digit == number[n + half_len]:
        sum_digits_2 += int(digit)

for n, digit in enumerate(number[half_len:]):
    if digit == number[n]:
        sum_digits_2 += int(digit)

print(sum_digits_2)
