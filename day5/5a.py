import hashlib

# Get input
with open('day5.txt', 'r') as f:
    input = f.readline()

count = 0
password = ""
while True:
    # Python 2.7.10 hashlib
    hashed_string = hashlib.md5(input + str(count)).hexdigest()
    if hashed_string[:5] == "00000":
        password += hashed_string[5]
        if len(password) == 8:
            print password
            quit()
    count += 1