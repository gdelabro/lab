x = 1

i = 2

old = 1

while len(str(x)) < 1000:
    truc = x
    x += old
    old = truc
    i += 1
print(i)
