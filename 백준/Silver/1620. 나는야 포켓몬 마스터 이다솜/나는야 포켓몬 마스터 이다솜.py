import sys
input = sys.stdin.readline
N, M = map(int, input().split())

itn = {}
nti = {}
for i in range(1, N + 1) :
    name = input().rstrip()
    itn[i] = name
    nti[name] = i
    
for _ in range(M) :
    query = input().rstrip()
    if query.isdigit() :
        print(itn[int(query)])
    else :
        print(nti[query])