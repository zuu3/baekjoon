N = int(input())
arr = [0] + [0] * N

if N > 0:
    arr[1] = 1
    for n in range(2,N+1):
        arr[n] = arr[n-1] + arr[n-2]
print(arr[-1])