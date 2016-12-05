import collections

key = "abcdefghijklmnopqrstuvwxyz"

with open('day4.txt', 'r') as f:
    sector_sum = 0
    for line in f:
        # Split string
        encrypted_name = line.split('[')[0].rsplit('-', 1)[0]
        sector_id = line.split('[')[0].rsplit('-', 1)[1]
        checksum = line[line.find("[") + 1:line.find("]")]

        # Decrypt
        decrypted_name = ""
        for l in encrypted_name:
            try: 
                decrypted_name += key[(key.index(l) + int(sector_id)) % 26]
            except ValueError:
                decrypted_name += " "

        if "north" in decrypted_name:
            print(sector_id)
            quit()