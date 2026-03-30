# 1. memset 방식 <- 추천
a = [0] * 21
b = [[0] * 21 for _ in range(21)]

# 2. for
a = [0] * 21
for i in range(21):
    a[i] = 0

b = [[0] * 21 for _ in range(21)]
for i in range(21):
    for j in range(21):
        b[i][j] = 0