# a = input()
# print(a)

# number = input("숫자를 입력하세요: ")
# print(num)

# age = input("나이를 입력하세요: ")
# age = int(age)
# print(age + 1)

# height = input("키를 입력하세요(cm): ")
# height = float(height)
# print(height / 100)

# age = int(input("나이를 입력하세요: "))
# print(type(age))

# print("2026", "03", "29", sep="-")

# for i in range(10):
#     print(i, end=' ')

print("=== 간단한 계산기===")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("첫 번째 숫자를 입력하세요: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if (num2 != 0):
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")