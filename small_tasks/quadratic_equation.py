from const import *


def numbers_equal(compare_what: numeric, compare_with: numeric) -> bool:
    if abs(compare_what - compare_with) < FLOAT_ERROR_DELTA:
        return True
    return False


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple:
    if numbers_equal(a, 0):
        raise ValueError(ZERO_A_PARAMETER_ERROR_MSG)

    discriminant = b ** 2 - 4 * a * c
    if numbers_equal(discriminant, 0):
        return - b / 2 * a,

    if discriminant < 0:
        return ()

    return (-b + discriminant ** 0.5) / 2 * a, (-b - discriminant ** 0.5) / 2 * a


if __name__ == '__main__':
    print(solve_quadratic_equation(1, 1, -2))

