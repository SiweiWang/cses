#! /usr/bin/python3
x = int(input())

for n in range(1, x+1):
    if n == 1:
        print(0)
    else:
        print(int(n*n*(n*n-1)/2 - 4*(n-1)*(n-2)))