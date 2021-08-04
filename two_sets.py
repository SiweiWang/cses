#! /usr/bin/python3
n = int(input())

sum = n*(n+1) //2

if sum % 2 == 0:
    target = sum //2
    a = set()
    b = set()
    for i in range(n, 0, -1):
        if i <= target:
            target -= i
            a.add(i)
        else:
            b.add(i)

    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print("NO")