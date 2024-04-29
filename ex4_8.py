#!/usr/bin/env python3


def solve():
    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result

from math import sqrt

# Perimeter
perimeter = 24

# Generate all possible combinations of side lengths
triangles = [(a, b, perimeter - a - b) for a in range(1, 11) for b in range(1, 11)]

# Filter out combinations where all side lengths are less than or equal to 10 cm
triangles = [(a, b, c) for (a, b, c) in triangles if c <= 10]

# Filter out combinations where a^2 + b^2 = c^2 (forming a right triangle)
triangles = [(a, b, c) for (a, b, c) in triangles if a**2 + b**2 == c**2]

print(triangles)