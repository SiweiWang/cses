n = int(input())

print(n * (n+1) // 2 - sum([int(x) for x in input().split()]))