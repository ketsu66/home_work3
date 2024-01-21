# 1
# name = input("Input your name: ")
# try:
#     age = int(input("Input your age: "))
#     if age < 0 or age > 130:
#         raise ValueError
#     else:
#         print(f"Hello, {name}, your age is {age}")
# except ValueError:
#     print("Error")
# 2
# def firstException():
#         raise ValueError
#
#
# name = input("Input your name: ")
# try:
#     age = int(input("Input your age: "))
#     if age < 0 or age > 130:
#         firstException()
#     else:
#         print(f"Hello, {name}, your age is {age}")
# except ValueError:
#     print("Error")


# def secondException(age: int):
#     try:
#         if age < 0 or age > 130:
#             raise ValueError
#         else:
#             print(f"Hello, {name}, your age is {age}")
#     except ValueError:
#         print("Error")
#
#
#
# age = int(input("Input your age: "))
# name = input("Input your name: ")
# secondException(age)
# 3
# i = 0
# myLst = []
# while i < 10:
#     try:
#         digit = int(input("Input digit > 0: "))
#         i += 1
#         digit = float(digit)
#         myLst.append(digit)
#         if digit < 0:
#             raise ValueError
#         else:
#             print(myLst)
#             print(sum(myLst))
#     except ValueError:
#         print("Error")
# 4
# def firstException():
#     raise ValueError
# i = 0
# myLst = []
# while i < 10:
#     try:
#         digit = int(input("Input digit > 0: "))
#         i += 1
#         digit = float(digit)
#         myLst.append(digit)
#         if digit < 0:
#             firstException()
#         else:
#             print(myLst)
#             print(sum(myLst))
#     except ValueError:
#         print("Error")

# def secondException(i):
#     i = 0
#     myLst = []
#     try:
#         while i < 11:
#             digit = int(input("Input digit > 0:"))
#             digit = float(digit)
#             myLst.append(digit)
#             i += 1
#             if digit < 0:
#                 raise ValueError
#             else:
#                 print(myLst)
#                 print(sum(myLst))
#     except ValueError:
#         print("Error")
#
# digit_2 = int(input("Input digit > 0: "))
# secondException(digit_2)