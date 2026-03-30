s = input()

freq = [0] * 26

for c in s:
    freq[ord(c) - ord('a')] += 1

for i in range(26):
    print(freq[i], end=' ')