registers = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0
}

def readRegister(x):
    try:
        return int(x)
    except:
        return registers[x]

with open('day23.txt', 'r') as f:
    instructions = [x.strip().split() for x in f.readlines()]

ip = 0

while ip < len(instructions):
    instruction = instructions[ip]
    if instruction[0] == "cpy":
        registers[instruction[2]] = readRegister(instruction[1])
    if instruction[0] == "inc":
        registers[instruction[1]] += 1
    if instruction[0] == "dec":
        registers[instruction[1]] -= 1
    if instruction[0] == "jnz":
        if readRegister(instruction[1]):
            ip += readRegister(instruction[2]) - 1
    if instruction[0] == "tgl":
        index = ip + readRegister(instruction[1])
        if index < 0 or index >= len(instructions):
            ip += 1
            continue
        if instructions[index][0] == "inc":
            instructions[index][0] = "dec"
        elif instructions[index][0] == "dec":
            instructions[index][0] = "inc"
        elif instructions[index][0] == "jnz":
            instructions[index][0] = "cpy"
        elif instructions[index][0] == "cpy":
            instructions[index][0] = "jnz"
        elif instructions[index][0] == "tgl":
            instructions[index][0] = "inc"
        else:
            print "Instruction exception"
    ip += 1

print registers