from typing import any


def cube(numbera: int) -> int:
    return number * number * number


def by_three(number: int) -> any:
    if number % 3 == 0:
        return cube(number)
    return False
