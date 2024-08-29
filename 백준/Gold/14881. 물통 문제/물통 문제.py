import math
def waterOk(a,b,c) :
    if c > max(a,b) :
        return "NO"
    if c % math.gcd(a,b) == 0 :
        return "YES"
    else :
        return "NO"

T = int(input())
for _ in range(T) :
    a,b,c = map(int, input().split())
    print(waterOk(a,b,c))