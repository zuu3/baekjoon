import sys
N = int(input())

for _ in range(N):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    rwords = []

    for word in words:
        rwords.append(word[::-1])

    ans = " ".join(rwords)
    print(ans)