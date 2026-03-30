s = input()

result = []
for c in range(ord('a'), ord('z') + 1):
    result.append(s.count(chr(c)))

print(*result)