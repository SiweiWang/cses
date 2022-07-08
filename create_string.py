#! /user/bin/python3
s = str(input())

letters = list(s)

words = set()

def generate(word, letters):
    if len(letters) == 1:
        words.add(word + letters[0])
    else:
        for i in range(len(letters)):
            generate(word + letters[i], letters[0:i] + letters[i+1:])

generate("", letters)
words = sorted(words)
print(len(words))
print("\n".join(words))