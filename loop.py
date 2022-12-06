# lsta=[1,2,3,4,5,6]
# for i in range(1,101):
#     print(i)

# range(start,stop,step)
# range(10)->start=0 stop=9 step=1
# range(1,10)->start=1 stop=9 step=1
# range(1,10,2)->start=1 stop=9 step=2

# list1 = list(range(1, 21))
# total = 0
# for i in list1:
#     total = total + i

# print(total)
# # print sum of multiples of 3 or 5 between 1 to 100

# totalofmultiples = 0
# for i in range(100):
#     if (i % 3 == 0) or (i % 5 == 0):
#         totalofmultiples += i

# print(totalofmultiples)
# a = 1
# while a <= 10:
#     print(f"{a} times looped")
#     a += 1

# Take username and password as input until user provide correct ones
# initial username=abc@gmail.com password=12345
# username = "abc@gmail.com"
# password = "12345"
# userinp = input("Please Enter USername:")
# userpass = input("Please Enter Password:")
# while userinp != username or userpass != password:
#     userinp = input("Please Enter USername:")
#     userpass = input("Please Enter Password:")
# print("success")

# a = {"first": "Chicken", "second": "Egg", "Dashain": "Tihar"}
# for x, y in a.items():
#     print(f"Keys={x}, Values={y}")

#
# a = {
#     "properties": {
#         "profile": {
#             "name": "Ram",
#             "education": [
#                 {"college": "ABC", "year": "2018"},
#                 {"college": "XYZ", "year": "2020"},
#             ],
#         },
#         "followers": 1000,
#         "following": 100,
#     }
# }
# name = a.get("properties").get("profile").get("name")
# followers = a.get("properties").get("followers")
# following = a.get("properties").get("following")
# Educations = a.get("properties").get("profile").get("education")
# print(f"Name={name}")
# print(f"Followers={followers}")
# print(f"Following={following}")
# for education in Educations:
#     year = education.get("year")
#     college = education.get("college")
#     print(f"Education({year}):{college}")

oil_prices = [
    {
        "oil_type": "petrol",
        "prices": [
            {"year": "2018", "price": 100},
            {"year": "2019", "price": 120},
            {"year": "2020", "price": 180},
        ],
    },
    {
        "oil_type": "diesel",
        "prices": [
            {"year": "2018", "price": 80},
            {"year": "2019", "price": 100},
            {"year": "2020", "price": 160},
        ],
    },
]
# sump = 0
# sumd = 0
# oiltype = oil_prices[0].get("oil_type").capitalize()
# prices = oil_prices[0].get("prices")
# print("---------------------------------------------")
# print(f"Oil Type:{oiltype}")
# for price in prices:
#     year = price.get("year")
#     price = price.get("price")
#     print(f"Year({year}):Rs.{price}")

# print("---------------------------------------------")
# oil_sec = oil_prices[1].get("oil_type").capitalize()
# die_prices = oil_prices[1].get("prices")
# print(f"Oil Type:{oil_sec}")
# for price in die_prices:
#     year = price.get("year")
#     price = price.get("price")
#     print(f"Year({year}):Rs.{price}")
print("-" * 50)
for oil in oil_prices:

    sumprice = 0
    print(f"Oil Type: {oil.get('oil_type').capitalize()}")
    print("-" * 50)
    prices = oil.get("prices")
    for items in prices:
        year = items.get("year")
        price = items.get("price")
        print(f"Year({year}):Rs.{price}")
        sumprice += price
    average = sumprice / len(prices)
    print(f"Average Price of {oil.get('oil_type').capitalize()}(2018-2020)={average}")
