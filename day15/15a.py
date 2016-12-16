# http://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('day15.txt', 'r') as f:
    inputText = map(str.split, f.readlines())

discs = [int(x[1][1]) for x in inputText]
numDiscPositions = [int(x[3]) for x in inputText]
startState = [int(x[11][:-1]) for x in inputText]

discInfo = zip(discs, numDiscPositions, startState)

a =[(x[1] - x[2] - x[0])%x[1] for x in discInfo]

print chinese_remainder(numDiscPositions, a)