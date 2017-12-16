net = []
for line in open('input.txt'):
    left, sep, neighbors = line.partition(' <-> ')
    neighbors = [int(n) for n in neighbors.split(', ')]
    net.append(neighbors)

start = 0
reachable = {start}
done = False
while not done:
    front = []
    for r in reachable:
        for n in net[r]:
            if n not in reachable:
                front.append(n)
    if len(front) == 0:
        done = True
    else:
        reachable.update(front)
part1 = reachable

com = {num for num in range(len(net))}
count = 0
while len(com) > 0:
    reachable = {com.pop()}
    done = False
    while not done:
        front = []
        for r in reachable:
            for n in net[r]:
                if n not in reachable:
                    front.append(n)
        if len(front) == 0:
            done = True
        else:
            reachable.update(front)
    com.difference_update(reachable)
    count += 1

print("Part 1:", len(part1))
print("Part 2:", count)
