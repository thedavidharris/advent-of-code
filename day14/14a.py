from hashlib import md5
from collections import defaultdict
import re

salt = "zpqevtbw"

hashes = []
matchingThrees = defaultdict(list)

index = 0

while len(hashes) < 64:
    valueToHash = salt + str(index)
    hash = md5(valueToHash).hexdigest()

    matchFive = re.search("(.)\\1{4}", hash)

    if matchFive:
        repeatedValue = matchFive.group(0)[0]
        for matchIndex, value in matchingThrees[repeatedValue]:
            if index - matchIndex <= 1000:
                hashes.append((matchIndex, value))
                print "Found hash: " + str(matchIndex)
        matchingThrees[repeatedValue] = []

    matchThree = re.search(r"(.)\1{2}", hash)

    if matchThree:
        repeatedValue = matchThree.group(0)[0]
        matchingThrees[repeatedValue].append((index, hash))
        
    index += 1

print hashes[63]