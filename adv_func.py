# def outer():
#     print("Outer Function")

#     def inner():
#         print("Inner Function")

#     inner()


# outer()


# def function_name():
#     print("I am a Function")


# a = function_name  # a gets the reference to function_name()
# a()  # function_name is called with function signature


# def addition(n1, n2):
#     return n1 + n2


# a = addition
# a gets the reference to function_name()
# print(a(2, 3))
# function_name is called with function signature


# def welcome(name):
#     print(f"Welcome {name}")


# def bye(name):
#     print(f"Bye {name}")


# def greet(func):
#     func("Rosan")


# greet(welcome)
# greet(bye)


# def outer():
#     def inner():
#         print("Inner Function")

#     return inner


# i = outer()
# i()
# def increment(num):
#     def increase_by(factor):
#         return num + factor

#     return increase_by


# inc = increment(2123)
# print(inc(5555))


# def exp_dec(func):
#     def wrapper():
#         print("Before example called")
#         func()
#         print("After Example called")

#     return wrapper


# @exp_dec
# def welcome():
#     print("Welcome")


# welcome()  # because of the decorator when we call welcome it actually calls wrapper function


def smart_div(func):
    def wrappper(a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return func(a, b)

    return wrappper


@smart_div
def divid(a, b):
    return a / b


# print(divid(10, 5))
# print(divid(2, 0))


# a = lambda x, y: x + y
# print(a(10, 10))


# map   map(function, iterable)  stores value that is returned

# a = [1, 2, 3, 4, 5]
# final = map(lambda n: n + 1, a)
# print(list(final))

# filter  filter(function, iterable)
# function must return boolean   stores only those value that return true
# a = [2, 3, 4, 5, 6, 7, 8, 9]
# out = filter(lambda n: n % 3 == 0, a)
# print(list(out))

student_marks = [
    {"name": "ram", "score": 80},
    {"name": "Sita", "score": 75},
    {"name": "Shyam", "score": 40},
    {"name": "ab", "score": 35},
    {"name": "ram", "score": 80},
    {"name": "pq", "score": 65},
]

out = filter(lambda n: n.get("score") >= 40, student_marks)
print(list(out))
