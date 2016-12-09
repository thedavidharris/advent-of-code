import numpy

with open('day8.txt', 'r') as f:
    text = f.readlines()

screen = numpy.zeros((6,50), dtype=str)

for line in text:
    if line.startswith("rect"):
        locale = map(int, line.strip().split()[1].split("x"))
        screen[:locale[1], :locale[0]] = "#"
    elif line.startswith("rotate column"):
        locale = map(int, line.strip().split('=')[1].split(" by "))
        screen[:,locale[0]] = numpy.roll(screen[:,locale[0]], locale[1])
    elif line.startswith("rotate row"):
        locale = map(int, line.strip().split('=')[1].split(" by "))
        screen[locale[0]] = numpy.roll(screen[locale[0]], locale[1])

# Pretty print this
screen[screen == ''] = "."
print('\n'.join(''.join(row) for row in screen))