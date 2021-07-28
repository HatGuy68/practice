# Largest prime factor of a number

def largest_prime_factor(n):
    answer = -1

    while n%2 == 0:
        answer = 2
        n >>= 1

    while n%3 == 0:
        answer = 3
        n = n/3

    for i in range(5, int(n**0.5) + 1, 6):
        while n%i == 0:
            answer = i
            n /= i
        while n%(i+2) == 0:
            answer = i+2
            n /= (i+2)
    
    if n > 4:
        answer = n
    
    return int(answer)

print(largest_prime_factor(600851475143))