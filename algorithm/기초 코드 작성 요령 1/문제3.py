import math

def func3(N):
    sqrt_N = int(math.sqrt(N))
    if sqrt_N * sqrt_N == N:
        return 1
    return 0
print(func3(756580036))