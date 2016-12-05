import hashlib

# Get input
with open('day5.txt', 'r') as f:
    input = f.readline()

count = 0
password = list("--------")

while True:
    # Python 2.7.10 hashlib
    hashed_string = hashlib.md5(input + str(count)).hexdigest()
    if hashed_string[:5] == "00000":
        try:
            if password[int(hashed_string[5])] == "-":
                password[int(hashed_string[5])] = hashed_string[6]
                if "-" not in password:
                    print "".join(password)
                    quit()
        except Exception:
            pass
    count += 1