# Check whether a number is Happy or not
# a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit
# https://en.wikipedia.org/wiki/Happy_number

# 2021/03/11 - AP Class

number = int(input("Enter a Number: "))
result = number

# 10-happy numbers only have one cycle:
# 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ...
# https://en.wikipedia.org/wiki/Happy_number#10-happy_numbers
# when (result == 4) we've reached the mentioned cycle and we can end the loop.
while result != 1 and result != 4:
    digit = 0
    digitsSum = 0
    n = result
    while n > 0:
        digit = n % 10
        digitsSum = digitsSum + (digit * digit)
        n = n // 10
    result = digitsSum

print(number, "is a Happy Number") if result == 1 else print(number, "is an Unhappy Number")
