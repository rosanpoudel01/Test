# try:
#     #code
# except:
#     #code
# else:
#     #if try diesnot raise exception
# finally:
#     #always executes


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter Number: "))
    print(num1 + num2)
except ValueError:
    print("String cannot be converted to Integer ")

name = input("Enter name: ")
print(f"{name}")
