def fibonacci_even_sum(n):
    total = 0
    a,b = 0,1
    add = 0
    while b< n:
        a,b = b,a+b
        if b%2 == 0:
            add += b
    
    return add

print(fibonacci_even_sum(4000000))