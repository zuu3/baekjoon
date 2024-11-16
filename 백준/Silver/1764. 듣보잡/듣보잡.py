import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hear = set(input() for _ in range(N))
see = set(input() for _ in range(M))

result = sorted(hear & see)

print(len(result))
for i in result:
    print(i, end='')