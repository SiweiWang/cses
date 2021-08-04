#! /usr/bin/python3
inputStirng = input()
dict = {}
max = 0
last = ""
for char in inputStirng:
    if last == "":
        dict[char] = 1
        max = 1
    else:
        if char == last:
            dict[char] += 1
            if dict[char] > max:
                max = dict[char]
        else:
            dict[char] = 1

    last = char
print(max)