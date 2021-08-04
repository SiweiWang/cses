#! /usr/bin/python3
n = int(input())
input_list = [int(x) for x in input().split()]

def min_diff(index, a, b):
    if index >= len(input_list):
        return abs(a-b)
    
    # recusive call 
    return min(min_diff(index+1, a + input_list[index], b), min_diff(index+1, a, b + input_list[index]))

print(min_diff(0, 0, 0))
