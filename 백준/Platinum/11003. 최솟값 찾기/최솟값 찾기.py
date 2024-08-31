import sys
from collections import deque
input = sys.stdin.readline
deque = deque()

N,L = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):

    while deque and (deque[-1][1] > A[i]) :
        deque.pop()

    deque.append((i+1,A[i]))

    if (deque[-1][0] - deque[0][0] >= L) :
        deque.popleft()
    print(deque[0][1], end=' ')