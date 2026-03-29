def insert(idx, num, arr, length):
    for i in range(length, idx, -1):
        arr[i] = arr[i - 1]
    arr[idx] = num
    length += 1
    return length

def erase(idx, arr, length):
    for i in range(idx, length - 1):
        arr[i] = arr[i + 1]
    length -= 1
    return length

arr = [10, 50, 40, 30, 70, 20, 0, 0, 0, 0]
length = 6

length = insert(3, 60, arr, length)
print(arr[:length])

length = erase(4, arr, length)
print(arr[:length])