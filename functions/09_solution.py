

# 1 2 3 4 5 6 7 8 9 10 

def even_generater(num):
    for i in range(2, num +1, 3):
        yield i


for item in even_generater(10):
    print(item)