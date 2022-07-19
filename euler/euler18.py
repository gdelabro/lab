with open("pyramide", "r") as f:
    pyramide = f.readlines()
    lines = [[int(e) for e in i.split()] for i in pyramide]
    for i in range(1, len(lines)):
        for e in range(0, len(lines[i])):
            if e == 0:
                lines[i][e] += lines[i - 1][e]
            elif e == len(lines[i]) - 1:
                lines[i][e] += lines[i - 1][e - 1]
            elif lines[i - 1][e] > lines[i - 1][e - 1]:
                lines[i][e] += lines[i - 1][e]
            else:
                lines[i][e] += lines[i - 1][e - 1]
max = 0
for i in lines[-1]:
    if i > max:
        max = i
print(max)
