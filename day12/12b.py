registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

def readRegister(x):
    try:
        return int(x)
    except:
        return registers[x]

with open('day12.txt', 'r') as f:
    instructions = f.readlines()
instructions = [x.strip().split() for x in instructions]

ip = 0

while ip < len(instructions):
    instruction = instructions[ip]
    if instruction[0] == "cpy":
        registers[instruction[2]] = readRegister(instruction[1])
    if instruction[0] == "inc":
        registers[instruction[1]] += 1
    if instruction[0] == "dec":
        registers[instruction[1]] -= 1
    if instruction[0] =="jnz":
        if readRegister(instruction[1]):
            ip += readRegister(instruction[2]) - 1

    ip += 1

print registers['a']