def fact(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    return fact(x - 1) * x

x = fact(100)
res = 0
for i in str(x):
    res += int(i)
print(res)
