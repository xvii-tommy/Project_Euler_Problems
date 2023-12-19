# A Pythagorean triplet is a set of three natural numbers a < b < c, for which, a^2 + b^2 = C^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product of abc
import math
answer = 0

for a in range(1, 500):
    for b in range(1, 500):
        c_sqrd = a ** 2 + b ** 2
        c = math.sqrt(c_sqrd)
        if a + b + c == 1000 and a * b * c != answer:
            answer = a * b * c
            print("The produce of a", a,"b", b,"c", c,"is", answer)
