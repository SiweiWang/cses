#! /usr/bin/python3
n = int(input())
data = [int(x) for x in input().split()]
total = 0
for i in range(1, n):
    if data[i] < data[i-1]:
        diff = data[i-1] - data[i]
        total += diff
        data[i] =  data[i-1]
print(total)