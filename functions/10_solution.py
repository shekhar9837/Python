

factorial =5
#  5 * 4 * 3 * 2 * 1

# factorial(5)
# num * i
# 5 * 1

# using loop

# result = 1
# number =5

# for i in range(1, number+1, 1):
#     result *= i
# print(result)

# usign recursive fn

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))