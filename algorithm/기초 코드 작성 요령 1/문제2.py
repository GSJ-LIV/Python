def func2(arr, N):
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == 100:
                return 1
    return 0

print(func2([1, 52, 48], 3))