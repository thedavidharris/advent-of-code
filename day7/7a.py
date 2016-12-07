def isCode(quadgram):
    return quadgram[0] == quadgram[3] and quadgram[1] == quadgram[2] and quadgram[0] != quadgram[1]

def foundCode(address):
    if len(address) < 4:
        return False
    else:
        return any(isCode(quadgram) for quadgram in zip(address, address[1:], address[2:], address[3:]))

tlsCount = 0
with open('day7.txt', 'r') as f:
    text = f.readlines()

for line in text:
    supportsTLS = False
    for index, section in enumerate(line.replace("[", "]").split("]")):
        # Inside brackets
        if index % 2 and foundCode(section):
            supportsTLS = False
            break
        # Outside brackets
        elif foundCode(section):
            supportsTLS = True
    tlsCount += supportsTLS

print(tlsCount)