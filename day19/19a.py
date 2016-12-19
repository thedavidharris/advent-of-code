with open('day19.txt', 'r') as f:
        n = int(f.readline())

# Binary Shift Method
print int(bin(n)[3:] + bin(1)[3:], 2) * 2 + 1




