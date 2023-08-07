def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(b, a)
    else:
        return gcd(a, b - a)
print(gcd(12, 18))