""""
multiply_numbers is a function that takes two arbitrary long numbers and returns their product as a string.
It resembles the way we count a product on a sheet of paper- first we find every subproduct of multiplying number2
by every digit in number1 and then we add those together by shifting every next subproduct by one position to the left.
For this reason we use the variable shift as a counter. Lines 14-25 calculate the subproducts and lines 26-51 add those
subproducts together.
"""


def multiply_numbers(number1, number2):
    number1 = ''.join(reversed(str(number1)))
    number2 = ''.join(reversed(str(number2)))
    new_number = ''
    shifts = 0
    if number1 == '0' or number2 == '0':
        return "0"
    for i in number2:
        carry = 0
        temporary_number = ''
        for j in number1:
            digit = int(i) * int(j)
            if len(temporary_number) >= len(number1) - 1:
                temporary_number = str(digit + carry) + temporary_number
            else:
                temporary_number = str(digit % 10 + carry) + temporary_number
                carry = digit // 10
        if new_number == '':
            new_number = temporary_number
            shifts += 1
        else:
            counter = 0
            new_number = ''.join(reversed(new_number))
            temporary_number = ''.join(reversed(temporary_number))
            next_number = new_number[:shifts]
            new_number = new_number[shifts:]
            shifts += 1
            while new_number or temporary_number:
                if new_number == '':
                    next_digit = int(temporary_number[:1])
                    next_number = str(next_digit + counter) + next_number
                    temporary_number = temporary_number[1:]
                elif temporary_number == '':
                    next_digit = int(new_number[:1])
                    next_number = str(next_digit + counter) + next_number
                    new_number = new_number[1:]
                else:
                    next_digit = int(new_number[:1]) + int(temporary_number[:1])
                    next_number = str(next_digit % 10 + counter) + next_number
                    counter = next_digit // 10
                    temporary_number = temporary_number[1:]
                    new_number = new_number[1:]
            new_number = next_number
    return new_number


# test with a 0 parameter

print(multiply_numbers(0, 300))

# test whether the returned value is of type string

print(type(multiply_numbers(155, 322)))

# test with parameters that are out of integer range

print(multiply_numbers(4000000000, 3000000000))

