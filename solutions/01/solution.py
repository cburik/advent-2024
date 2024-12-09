with open("input.txt") as f:
    data = f.readlines()

l1 = []
l2 = []

for r in data:
    x, y = r.split()
    l1.append(int(x))
    l2.append(int(y))

l1.sort()
l2.sort()

s = 0
s = sum(abs(x - y) for x, y in zip(l1, l2))

print(s)

s = 0
s = sum(x * sum(1 for y in l2 if x == y) for x in l1)

print(s)
