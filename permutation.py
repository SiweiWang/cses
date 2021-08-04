#! /usr/bin/python3
n = int(input())
if n == 1:
    print(n)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    s = ""
    for i in range(2, n+1, 2):
        s += "{} ".format(i)
    for i in range(1, n+1, 2):
        s += "{} ".format(i)
    print(s.strip())