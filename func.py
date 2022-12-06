# def function_name():
#     print("I am Function!!!!")


# function_name() function is executed
# function_name   reference is passed


# def profile(name, contact, address):
#     print(f"Name: {name}")
#     print(f"Contact: {contact}")
#     print(f"Address:{address}")


# # positional arguments
# profile("Ram", "9845213", "Bkt")
# # keyword argument
# profile(name="Hari", address="biratnager", contact="9845554")


# def exponent(base, power=2):  # default argument
#     print(base**power)


# exponent(2)  # uses default arugment
# exponent(5, 3)  # uses passed argument


# def addition(a, b):
#     print(a + b)


# def product(a, b):
#     prod = a * b
#     return prod


# suum = addition(10, 12)
# print(suum)
# res = product(10, 12)
# print(res)


# def newfunc(*a):  multiple arguments support args
#     for i in a:
#         print(i)


# newfunc(1, 2, 3, 4, 5, 6)


# def new_func(**b): converts to a dict  of keyword argument kwrgs
#     print(b)
# packing into a dictionary

# new_func(name="Ram", contact="998855", age="15")


# def profile(name, contact, address):
#     print(f"Name: {name}")
#     print(f"Contact: {contact}")
#     print(f"Address:{address}")


# a = {"name": "Shyam", "contact": "89955", "address": "ktm"}
# profile(**a)
# unpacking from a dictionary
