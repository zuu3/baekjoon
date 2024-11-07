a = input().split(",")
sum = 0
for i in a:
    if i.isdigit():
        sum += 1
print(sum)