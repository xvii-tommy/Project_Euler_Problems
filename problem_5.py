# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that evenly divisible by all of the numbers from 1 to 20

pf_powers = []
pf_value = []
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

for num in range(2, 20):
    array_prime_factors = find_prime_factors(num)
    solution = prime_factorisation(num, array_prime_factors)
    pf_powers.append(solution)

for i in range(0, len(pf_powers)):
    for j in range(0, len(pf_powers[i])):
        pf_value.append(pf_powers[i][j])

x = []
# set to remove duplicates
pf_set = set(pf_value)
val = 0
count = 1
# count how many prime factors are in a row to get the largest power
# append to x the value of the prime factor with the largest power
for y in pf_set:
    for z in range(0, len(pf_value) - 1):
        if pf_value[z] == pf_value[z + 1] and pf_value[z] == y:
            count += 1
        elif pf_value[z] != pf_value[z + 1]:
            if y * count > val:
                val = y * count
    x.append(val)
    val = 0
    count = 1

total = 1

# mutliply values together
for t in x:
    total = t * total
    print(total)

