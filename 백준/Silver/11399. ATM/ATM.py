N = int(input())
M = list(map(int, input().split()))

M.sort()
total = 0
for i in range(1, N+1) :
    total += sum(M[:i])
print(total)