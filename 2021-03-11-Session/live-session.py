number = int(input())


def squared_digits_sum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = digit * digit + sum
        n = n // 10
    return sum


result = squared_digits_sum(number)
while result != 1 and result != 4:
    result = squared_digits_sum(result)

if result == 1:
    print('yeeeeeees!')
else:
    print('nooooooo!')
