def divs(m):
    divset = set()
    for n in range(1, m+1):
        if m % n == 0:
            divset.add(n)
    return divset

divs12 = divs(12)
divs18 = divs(18)
print(divs12 & divs18)