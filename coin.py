#! /usr/bin/python3

n = int(input())
for _ in range(n):
    data = [int(x) for x in input().split()]
    if (data[0] + data[1]) % 3 !=0 or data[0] > 2 * data [1] or data[1] > 2 * data[0]:
        print ("NO")
    else:
        print("YES")
