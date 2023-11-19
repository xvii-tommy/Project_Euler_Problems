# By listing the first six prime numbers you get: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def find_prime_number(number):
    pf = []
    solved = False
    i = 1
    while solved == False:
        i = i + 1
        x = is_prime(i)
        if x == True:
            pf.append(i)
        if len(pf) == number:
            solved = True
    return(pf[-1])
def is_prime(num):
    j = 1
    is_prime = True
    while j * 2 < num and is_prime == True:
        j = j + 1
        if num % j == 0:
            is_prime = False
    return(is_prime)

print(find_prime_number(10001))