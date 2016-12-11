import re, collections

botDict = collections.defaultdict(list)
outputDict = collections.defaultdict(list)

destinations = {
    "bot": botDict,
    "output": outputDict
}

with open('day10.txt', 'r') as f:
    inputText = f.readlines()

instructions = {}
for line in inputText:
    if line.startswith('value'):
        value, botnum = [int(s) for s in line.split() if s.isdigit()]
        botDict[botnum].append(value)
    if line.startswith('bot'):
        giveBot, lowChip, highChip = [int(s) for s in line.split() if s.isdigit()]
        lowDest, highDest = re.findall(r' (bot|output)', line)
        instructions[giveBot] = (lowDest, lowChip),(highDest, highChip)

while botDict:
    for key, value in dict(botDict).items():
        if len(value) == 2:
            chips = botDict.pop(key)
            low, high = sorted(chips)
            (lowDest, lowChip),(highDest, highChip) = instructions[key]
            destinations[lowDest][lowChip].append(low)
            destinations[highDest][highChip].append(high)

print(reduce(lambda x, y: x*y, (outputDict[x][0] for x in [0,1,2])))            