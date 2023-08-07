m = input("무슨 수의 약수를 구하고 싶나요? ")
m = int(m)
divs = []
for n in range(1, m+1):
    if m % n == 0:
        divs.append(n)
print(f"{m}의 약수는 {divs}입니다.")