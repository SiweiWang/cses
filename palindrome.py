#! /usr/bin/python3

s = str(input())
char_map = {}
for char in s:
    if char not in char_map:
        char_map[char] = 1
    else:
        char_map[char] += 1


left = ""
centre = ""
right = ""
number_of_odd = 0
for key in char_map:
    if char_map[key] % 2 == 0:
        left += key * (char_map[key] // 2)
        right = key * (char_map[key] // 2)  + right
    else:
        number_of_odd +=1
        centre =  key * char_map[key]

if number_of_odd > 1:
    print("NO SOLUTION")
else:
    print(left + centre + right)