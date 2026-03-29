# def add(a, b):
#     return a + b

# a = 3
# b = 4
# c = add(a, b)
# print(c)

# def say():
#     return 'HI'

# a = say()
# print(a)

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a , b, a + b))

# (add(3, 4))

# def say():
#     print('HI')

# say()

# def sub(a, b):
#     return a - b

# result = sub(b = 5, a = 3)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(add_many(1, 2, 3, 4))

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result

# print(add_mul("add", 1, 2, 3, 4))
# print(add_mul("mul", 1, 2, 3, 4))

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)
# print_kwargs(name='foo', age=3)
# print_kwargs(name='홍길동', age=25, city='서울', job='개발자')

# def create_profile(**info):
#     print("=== 프로필 정보 ===")
#     for key, value in info.items():
#         print(f"{key}: {value}")

# create_profile(이름="김철수", 나이=30, 직업="프로그래머", 취미="독서")

# def mixed_function(name, *args, **kwargs):
#     print(f"이름: {name}")
#     print(f"추가 인수들: {args}")
#     print(f"키워드 인수들: {kwargs}")

# mixed_function('홍길동', 1, 2, 3, age=25, city='서울')

# def add_and_mul(a, b):
#     return a+b, a*b

# result = add_and_mul(3, 4)
# resul1, result2 = add_and_mul(3, 4)

# def add_and_mul(a, b):
#     return a+b
#     return a*b

# result = add_and_mul(2, 3)
# print(result)

# def say_myself(name, age, man=True):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자압니다.")
#     else:
#         print("여자입니다.")

# say_myself("고강현", 27)
# say_myself("고강현", 27, True)
# say_myself("고강현", 27, False)

# def say_myself(name, man=True, age):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자압니다.")
#     else:
#         print("여자입니다.")

# say_myself("박준용", 27)

# a = 1
# def vartest(a):
#     a += 1

# vartest(a)
# print(a)

# def vartest(a):
#     a += 1

# vartest(3)
# print(a)

# a = 1
# def vartest(a):
#     a += 1
#     return a

# a = vartest(a)
# print(a)

# def change_list(my_list):
#     my_list.append(4)

# a = [1, 2, 3]
# change_list(a)
# print(a)

# add = lambda a, b: a + b
# result = add(3, 4)
# print(result)

# def add (a, b):
#     """
#     두 숫자를 더하는 함수

#     Parameter:
#     a (int, float): 첫 번째 숫자
#     b (int, float): 두 번째 숫자

#     Retruns:
#     int, float: 두 숫자의 합
#     """
#     return a + b

# print(add.__doc__)