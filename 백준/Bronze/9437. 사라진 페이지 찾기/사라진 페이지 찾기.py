while True:
    n = list(map(int, input().split()))
    if n == [0]:
        break
    for i in range(n[0]//4):
        li = [2*i+1, 2*i+2, n[0]-2*i-1, n[0]-2*i]
        if n[1] in li:
            li.remove(n[1])
            print(*li)