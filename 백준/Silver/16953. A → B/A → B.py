from collections import deque
import sys
input = sys.stdin.readline

def solve(a,b) :
    q = deque([(a,1)])

    while q :
        now, cnt = q.popleft()
        if now == b :
            print(cnt)
            return

        if now <= b :
            q.append((now * 2, cnt+1))
        if now <= b :
            q.append((now * 10 + 1, cnt+1))
    print(-1)

a,b = map(int, input().split())
solve(a,b)