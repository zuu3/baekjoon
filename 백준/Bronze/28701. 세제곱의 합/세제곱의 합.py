import sys
input = sys.stdin.readline

n = int(input())

one = 0
three = 0

for i in range(1, n+1):
    one += i
    three += i**3

print(one)
print(one**2)
print(three)