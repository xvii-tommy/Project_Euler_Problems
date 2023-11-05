#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009.
#Find the largest palindrome made from the product of two 3-digit numbers.

biggest_pal = 0

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        number = str(i * j)
        reverse_number = str(number[::-1])
        reverse_number = int(reverse_number)
        number = int(number)
        if number == reverse_number and number > biggest_pal:
            biggest_pal = number
print("The largest palindromic number is", biggest_pal)