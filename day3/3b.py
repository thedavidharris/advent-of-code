from itertools import islice

triangles = []
# Parse input and create array of triangles
with open('day3.txt', 'r') as f:
    triangles = []
    # Read through 3 lines at a time
    while True:
        next_3_lines = [x.strip().split() for x in list(islice(f,3))]
        if not next_3_lines:
            break
        for i in range(0,3):
            triangles.append([int(next_3_lines[0][i]),
                            int(next_3_lines[1][i]),
                            int(next_3_lines[2][i])])

numPossible = 0     
for triangle in triangles:      
    numPossible += 2 * max(triangle[0], triangle[1], triangle[2]) < triangle[0] + triangle[1] + triangle[2]
print numPossible