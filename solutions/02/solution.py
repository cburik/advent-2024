with open("input.txt") as f:
    data = f.readlines()

s = 0
for r in data:
    l = r.split()
    l0 = l.pop(0)
    l0 = int(l0)
    safe = True
    inc = None
    for x in l:
        x = int(x)
        if abs(l0 - x) > 3 or abs(l0 - x) < 1:
            safe = False
        if inc is None:
            if l0 - x < 0:
                inc = True
            else:
                inc = False
        else:
            if inc and l0 - x > 0:
                safe = False
            if not inc and l0 - x < 0:
                safe = False
        l0 = x
    if safe:
        s += 1

print(s)
