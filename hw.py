# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# num3 = int(input("Enter Third Number: "))
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is Greatest Number")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is Greatest Number")
# else:
#     print(f"{num3} is Greatest Number")


# print("The Greatest Number is", max(num1, num2, num3))


#
# number = int(input("Enter Number to check: "))
# if ((number % 3) == 0) and ((number % 5) == 0):
#     print("The number is divisible by 3 and 5 ")
# elif ((number % 3) == 0) and ((number % 7) == 0):
#     print("The number is divisible by 3 and 7 ")
# elif ((number % 5) == 0) and ((number % 7) == 0):
#     print("The number is divisible by 5 and 7 ")
# elif (number % 3) == 0:
#     print("The number is divisible by ")
# elif (number % 5) == 0:
#     print("The number is divisible by 5 ")
# elif (number % 7) == 0:
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 3 or 5 or 7")


main = []
even = []
odd = []
duplicate = []

# take user input 15 times append all input in main list
# append even number in even list
# append odd number in odd list
# append duplicate entry to duplicate list dont use set

# for i in range(15):    Rosan Poudel
#     a = int(input(f"Enter {i+1} number: "))
#     main.append(a)
#     if a % 2 == 0 and a not in even:
#         even.append(a)
#     elif a in even:
#         duplicate.append(a)
#     elif a % 2 != 0 and a not in odd:
#         odd.append(a)
#     elif a in odd:
#         duplicate.append(a)
# for i in range(15):
#     a = int(input(f"Enter {i+1} number: "))
#     if a in main:
#         duplicate.append(a)
#     else:
#         if a % 2 == 0:
#             even.append(a)
#         else:
#             odd.append(a)
#     main.append(a)


# print(main)
# print(even)
# print(odd)
# print(duplicate)

# colors = ["yellow", "green", "red", "blue", "yellow", "orange", "red"]
# to_be_removed = ["yellow", "red"]
# a = filter(lambda i: i not in to_be_removed, colors)

# b = list(a)
# print(b)

a = "876d59e45"
summ = 0
for i in a:
    if i.isnumeric():
        summ = summ + int(i)

print(summ)
print(sum(map(int, filter(str.isnumeric, a))))
