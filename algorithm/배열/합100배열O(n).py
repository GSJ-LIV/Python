def func2(arr, N):
    occur = [0] * 101

    for i in range(N):
        if occur[100 - arr[i]] == 1:
            return 1
        occur[arr[i]] = 1
    return 0

arr1 = [30, 50 , 70 , 10]
print(func2(arr1, 4))