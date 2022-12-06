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

for i in range(15):
    a = int(input("enter a number"))
    main.append(a)
print(main)

for i in main:
    if i % 2 == 0 and i not in even:
        even.append(i)
    elif i in even:
        duplicate.append(i)
print(even)
for i in main:
    if i % 2 != 0 and i not in odd:
        odd.append(i)
    elif i in odd:
        duplicate.append(i)
print(odd)
print(duplicate)
