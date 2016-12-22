from collections import deque
from itertools import permutations

def swapPosition(s, x, y):
    s[x], s[y] = s[y], s[x]
    return s

def swapLetters(s, x, y):
    i1, i2 = s.index(x), s.index(y)
    s[i1], s[i2] = s[i2], s[i1]
    return s

def rotateLeft(s, x):
    s = deque(s)
    s.rotate(-x)
    return list(s)

def rotateRight(s, x):
    s = deque(s)
    s.rotate(x)
    return list(s)

def rotateAboutPosition(s, x):
    s = deque(s)
    num = x + 2 if x >=4 else x + 1
    return rotateRight(s, num)

def reverse(s, x, y):
    s[x:y+1] = list(reversed(s[x:y+1]))
    return s

def move(s, x, y):
    l = s[x]
    del s[x]
    s.insert(y, l)
    return s

def unscramble(word, instructions):
    for i in instructions:
        if " ".join(i).startswith("swap position"):
            x, y = [int(x) for x in i if x.isdigit()]
            word = swapPosition(word,x,y)
        if " ".join(i).startswith("swap letter"):
            word = swapLetters(word, i[2], i[5])
        if " ".join(i).startswith("rotate left"):
            x = next(int(x) for x in i if x.isdigit())
            word = rotateLeft(word, x)
        if " ".join(i).startswith("rotate right"):
            x = next(int(x) for x in i if x.isdigit())
            word = rotateRight(word, x)
        if " ".join(i).startswith("rotate based"):
            word = rotateAboutPosition(word, word.index(i[-1]))
        if " ".join(i).startswith("reverse"):
            x, y = [int(x) for x in i if x.isdigit()]
            word = reverse(word, x, y)
        if " ".join(i).startswith("move"):
            x, y = [int(x) for x in i if x.isdigit()]
            word = move(word, x, y)
    return word

with open('day21.txt', 'r') as f:
    instructions = [x.strip().split() for x in f.readlines()]

scrambled = list('fbgdceah')
for p in permutations(scrambled):
    if unscramble(p, instructions) == scrambled:
        print "".join(p)
        break