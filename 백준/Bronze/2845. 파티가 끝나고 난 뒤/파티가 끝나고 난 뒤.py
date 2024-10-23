L, P = map(int, input().split())
li = list(map(int, input().split()))
for i in li:
    print(i - L * P, end = ' ')