# If we list all natural numbers below 10 that are mutliples of 3 or 5, we get 3,5,6 and 9.
# The sum of these mutliples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(top_value, m1, m2):
    sum = 0
    for i in range(top_value):
        if i % m1 == 0 or i % m2 == 0:
            sum = sum + i
    return(sum)

print(sum_of_multiples(1000, 3, 5))


