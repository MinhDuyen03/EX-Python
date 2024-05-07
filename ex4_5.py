#!/usr/bin/env python3


def solve(numbers):
    """Tính tổng và tích của dãy số `numbers`

#     Return một tuple (sum, product)
#     Không sử dụng hàm `sum`
#     """
def sum_and_product(numbers):
    sum = 0
    product = 1
    for num in numbers:
        sum = sum + num
        product *= num
    return sum, product

numbers = [1, 2, 3, 4]

sum, product = sum_and_product(numbers)
print("Sum:", sum)
print("Product:", product)

