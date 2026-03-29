# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()

# f = open("새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("새파일.txt", 'r')
# for line in f:
#     print(line)
# f.close()

# f = open("새파일.txt", 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

# with open("foo.txt", "w") as f:
#     f.write("Life too short, you need python")
#     print(f.closed)
# print(f.closed)

# if True:
#     if_var = "if 블록 안의 변수"
# print(if_var)

# for i in range(3):
#     loop_var = "반복문 안의 변수"

# print(i)
# print(loop_var)

# with open("test.txt", 'w') as f:
#     content = "Hello, Python!"
#     f.write(content)
# print(content)

with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)