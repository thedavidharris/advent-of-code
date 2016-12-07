def isCode(trigram):
    return trigram[0] == trigram[2] and trigram[0] != trigram[1]

def supportsSSL(inside, outside):
    # Find pattern in text outside bracket
    for outsideString in outside:
        for trigram in zip(outsideString, outsideString[1:], outsideString[2:]):
            if isCode(trigram):
                # Search code in brackets for right pattern
                code = trigram[1] + trigram[0] + trigram[1]
                for insideString in inside:
                    if code in insideString:
                        return True
    return False
    
with open('day7.txt', 'r') as f:
    text = f.readlines()

sslCount = 0

for line in text:
    inside = []
    outside = []
    
    for index, section in enumerate(line.replace("[", "]").split("]")):
        if index % 2:
            inside.append(section)
        else:
            outside.append(section)

    sslCount += supportsSSL(inside, outside)
    
print(sslCount)