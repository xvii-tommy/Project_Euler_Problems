#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

num1 = 0
num2 = 0

for i in range(0,101):
    num1 = num1 + i ** 2
    num2 = num2 + i
print(abs(num1 - num2 ** 2))