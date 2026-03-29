# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# marks = [90, 25, 67, 45, 80]

# number = 0

# for mark in marks:
#     number += 1
#     if mark < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % number)

# a = range(10)
# print(a)

# a = range(1, 11)
# print(a)

# add = 0
# for i in range(1, 11):
#     add += i
# print(add)

# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print('')

# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num*3)
# print(result)

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

# result = [x * y for x in range(2, 10)
#                 for y in range(1, 10)]
# print(result)

# for i in range(10):
#     if i  == 5:
#         break
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print("for 문이 정상 종료되었습니다.")

# fruits = ['apple', 'banana', 'orange']
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# names = ['홍길동', '김철수', '이영희']
# scores = [85, 92, 78]
# for name, score in zip(names, scores):
#     print(f"{name}, {score}점")

names = ['홍길동', '김철수', '이영희']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
    print(f"{name}:  국어 {kor}점, 영어 {eng}점")