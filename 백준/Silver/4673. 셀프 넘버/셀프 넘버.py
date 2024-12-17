def d(n) :
    return n + sum(map(int, str(n)))

sel = [False]*10001

for i in range(1, 10001) :
    val = d(i)
    if (val <= 10000) :
        sel[val] = True
    if not sel[i] : print(i)