import math
D, H, W = map(int, input().split())
k = D / math.sqrt(W**2 + H**2)

print(f'{int(H * k)} {int(W * k)}')