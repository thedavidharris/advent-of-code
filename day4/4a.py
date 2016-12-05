import collections

with open('day4.txt', 'r') as f:
    sector_sum = 0
    for line in f:
        # Split string
        encrypted_name = line.split('[')[0].rsplit('-', 1)[0].replace('-', '')
        sector_id = line.split('[')[0].rsplit('-', 1)[1]
        checksum = line[line.find("[") + 1:line.find("]")]

        # Get most common letters
        mostCommonLetters = sorted(collections.Counter(encrypted_name).most_common(), key=lambda k: (-k[1], k[0]))[:5]

        mostCommon5 = "".join([key[0] for key in mostCommonLetters])

        if checksum == mostCommon5:
            sector_sum += int(sector_id)

    print sector_sum