import numpy as np

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

########## Brute force approach ##########
primes = []

def is_prime(num):
    prime = True
    x = 2
    while prime == True and x < num:
        if num % x == 0:
            prime = False
        x += 1
    return(prime)

def prime_search(s,e):
    for num in range(s, e):
        p = is_prime(num)
        if p == True:
            primes.append(num)

#val = prime_search(1, 2000000)
#print(primes, sum(primes))


########## Using Sieve of Eratosthenes algorithm ##########
total = 0
num = 2000000

prime_numbers = [True for i in range(num + 1)]

p = 2
while p * p <= num:
    if prime_numbers[p] == True:
        for i in range(p ** 2, num + 1, p):
            prime_numbers[i] = False
    p += 1

for p in range(2, num + 1):
    if prime_numbers[p] == True:
        print(p)
        total = total + p

print(total)