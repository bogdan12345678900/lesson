# x = int(input("int X: "))
# y = int(input("int Y: "))
# res = 1
# for i in range(y):
#     res *= x
# print(res)

# count = 0
# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a == b:
#         print(i)
#         count +=1
#     elif b == c:
#         print(i)
#         count += 1
#     elif a == c:
#         print(i)
#         count += 1
# print(count)

# count = 0
# for i in range(100,10000):
#     if i < 1000:
#         a = i // 100
#         b = i // 10 % 10
#         c = i % 10
#         if a != b and a != c and b != c:
#             count += 1
#     else:
#         a = i // 1000
#         b = i // 100 % 10
#         c = i // 10 % 10
#         d = i % 10
#         if a != b and a != c and b != c and b != d and d != c and c != a:
#             count += 1
# print(count)

# a = int(input("число: "))
# new = 1
# while a>0:
#     temp = a % 10
#     a = a // 10
#     if temp == 3 or temp == 6:
#         continue
#     else:
#         new = temp + temp * 10
# print(new)
# for i in str(a):
#     if i == "3" or i == "6":
#         continue
#     else:
#         new += 1


# a = int(input("a: "))
# for i in range(a):
#     for j in range(0 ,i +1):
#         if i == 0 or i == j or j == 0 or a ==i or a == j or i == a-1:
#             print('*',end="")
#         else:
#             print(" ", end="")
#     print()

a = int(input("a: "))
for i in range(a):
    for j in range(0 ,i +1):
        if i == 0 or i == j or j == 0 or a ==i or a == j or i == a-1:
            print('*',end="")
        else:
            print(" ", end="")

    print()
