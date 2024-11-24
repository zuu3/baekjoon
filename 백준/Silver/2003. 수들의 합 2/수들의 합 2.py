N, M = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
s = 0
count = 0

while end < N:
    s += A[end]
    end += 1

    while s >= M:
        if s == M:
            count += 1
        s -= A[start]
        start += 1

print(count)