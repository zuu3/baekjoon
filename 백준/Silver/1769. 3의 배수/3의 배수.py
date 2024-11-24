import sys
input = sys.stdin.readline

n = input().strip()
total = 0

while len(n) > 1:
    n = str(sum(int(digit) for digit in n))
    total += 1

if int(n) % 3 == 0:
    print(total)
    print("YES")
else:
    print(total)
    print("NO")