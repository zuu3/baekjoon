from math import pow

def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
    else:
        hanoi(n-1, a, c, b)
        print(f"{a} {c}")
        hanoi(n-1, b, a, c)


n = int(input())
cnt = int(pow(2,n)) - 1
print(cnt)
if (n > 20) :
    pass
else :
    hanoi(n, 1,2,3)