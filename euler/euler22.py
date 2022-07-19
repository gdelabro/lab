def super_calcul(name):
    res = 0
    for i in name:
        res += ord(i) - ord('A') + 1
    return (res)

with open("p022_names.txt", "r") as f:
    lines = f.read().split(",")
    lines2 = [i.replace("\"","").replace("\n","") for i in lines]
    lines2.sort()
    result = 0
    for i in range(1, len(lines2) + 1):
        r = super_calcul(lines2[i - 1]) * i
        result += r
        print(lines2[i - 1],r,result,i)
    print(result)
