#  v1: 크기 3, 값 5로 초기화
v1 = [5] * 3
print(len(v1))
v1.append(7)

# v2: 크기 2, 값 0으로 초기화
v2 = [0] * 2
v2.insert(1, 3)

# v3: 직접 값 지정
v3 = [1, 2, 3, 4]
v3.pop(2)

# v4: 복사
v4 = []
v4 = v3.copy()
print(v4[0], v4[1], v4[2])
v4.pop()
v4.clear()

v1 = [1, 2, 3, 4, 5, 6]

# 1. range-based for loop
for e in v1:
    print(e, end=' ')

# 2. not bad
for i in range(len(v1)):
    print(v1[i], end=' ')

# 3. ***WRONG***
for i in range(len(v1) -1 + 1):
    print(v1[i], end=' ')