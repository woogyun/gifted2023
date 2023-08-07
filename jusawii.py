count = 0
for a in range(1, 7):
    for b in range(1, 7):
        c = a + b
        if c in [5, 6]:
            count += 1
            print(a, b)
print(count)
