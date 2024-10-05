A = int(input())
member = []

for idx in range(A):
    age, name = input().split()
    member.append([int(age), name, idx])

member.sort(key=lambda x: (x[0], x[2]))

for m in member:
    print(m[0], m[1])
