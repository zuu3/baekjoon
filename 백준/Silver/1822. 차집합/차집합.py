N, M = map(int, input().split())

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

result = sorted(s1 - s2)
print(len(result))
for i in result:
    print(i, end=' ')