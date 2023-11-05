# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that evenly divisible by all of the numbers from 1 to 20

def find_prime_factors(number):
    solved = False
    factors = []
    pf = []
    i = 1
    while solved == False and i * 2 <= number + 1:
        i = i + 1
        if number % i == 0:
            x = is_prime(i)
            if x == True:
                pf.append(i)
            elif x == False:
                factors.append(i)
                y = multiplyList(factors)
                if y >= number:
                    solved = True
    if len(pf) == 0:
        pf.append(number)
    return(pf)

def is_prime(num):
    j = 1
    is_prime = True
    while j * 2 < num and is_prime == True:
        j = j + 1
        if num % j == 0:
            is_prime = False
    return(is_prime)

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return(result)

def prime_factorisation(number, prime_factors):
    factorisation_results = []
    i = 1
    amount = number
    while i < number and amount > 1:
        i += 1
        if i in prime_factors and amount % i == 0:
            amount = amount / i
            factorisation_results.append(i)
            i = 1
    return(factorisation_results)

#num = int(input("What number would you like to find the prime factors for?"))
#array_prime_factors = find_prime_factors(num)
#solution = prime_factorisation(num, array_prime_factors)
#print(solution)