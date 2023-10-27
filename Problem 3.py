# the prime factors of 131195 are 5,7,13 & 29
#What's the larget prime factor of 600851475143

def find_factors(i = 0, number = 600851475143):
    factors = []
    while i * i < number:
        i = i + 1
        if number % i == 0:
            factors.append(i)

    for n in range((len(factors)-1), 0, -1):
        x = find_prime(2, factors[n])
        if x == False:
            factors.remove(factors[n])
    print(factors[-1], "is the largest prime factor of", number)

def find_prime(j, num):
    is_prime = True
    while j * j < num and is_prime == True:
        j = j + 1
        if num % j == 0:
            is_prime = False
    return(is_prime)

x = find_factors()