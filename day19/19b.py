with open('day19.txt', 'r') as f:
    n = int(f.readline())

stealer = 1
for i in xrange(1, n):
    stealer = stealer % i + 1
    if(stealer > (i+1)/2):
        stealer += 1
    
print stealer