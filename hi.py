# SUm of current number and number before
# prev_number = 0
# for i in range(1, 11):
#     prev_number = i + 1
#     summ = prev_number + i
#     print(summ)

# printing char from even position of a string
# name = "RosanPoudel"
# for i in range(0, len(name)):
#     if i % 2 == 0:
#         print(name[i])

a = "876d59e45"
summ = 0
for i in range(0, len(a)):
    if a[i].isnumeric():
        summ = summ + int(a[i])

print(summ)
