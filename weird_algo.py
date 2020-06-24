n = int(input())

print(n)
while n >1:
    if n % 2 == 1:
        n = n * 3 + 1
        print(n)
    else:
        n = n // 2
        print(n)