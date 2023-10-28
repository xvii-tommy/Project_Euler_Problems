# the prime factors of 131195 are 5,7,13 & 29
#What's the larget prime factor of 600851475143

# puts all factors in factors list
# Largest prime factor found is set to answer
# stops when all factors multiplied equal original number
def find_prime_factors(number):
    solved = False
    factors = []
    answer = 2
    i = 1
    while solved == False:
        i = i + 1
        if number % i == 0:
            x = is_prime(i)
            if x == True:
                answer = i
                factors.append(i)
            elif x == False:
                factors.append(i)
                y = multiplyList(factors)
                if y >= number:
                    solved = True
    return(answer)

# Checks all possible factors
# if none are found is_prime is true
def is_prime(num):
    j = 1
    is_prime = True
    while j * 2 < num and is_prime == True:
        j = j + 2
        if num % j == 0:
            is_prime = False
    return(is_prime)


# multiplies factors of a number
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return(result)


num = int(input("What number would you like to find the largets prime factor for?"))
solution = find_prime_factors(num)
print("The largest prime factor of", num, "is", solution)
