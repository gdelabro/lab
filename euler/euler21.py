def propor_divisors(x):
    l = []
    for i in range(1, x):
        if x % i == 0:
            l.append(i)
    return l

def sum_pd(x):
    l = propor_divisors(x)
    res = 0
    for i in l:
        res += i
    return res

def is_amical(x):
    if x == sum_pd(sum_pd(x)) and x != sum_pd(x):
        return True
    return False




res = 0
for i in range(1, 10001):
    if is_amical(i) == True:
        res += i
print(res)
