# Multiples of 3 or 5

def mul_3_5(limit):
    add = 0
    i = 0
    while i<limit:
        if (i%3 == 0) or (i%5==0):
            add += i
        i+=1
    
    return add

print(mul_3_5(1000))