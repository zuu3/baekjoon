n = int(input())

s = set(map(int, input().split()))

result = sorted(s)

for i in result :
    print(i, end= ' ')