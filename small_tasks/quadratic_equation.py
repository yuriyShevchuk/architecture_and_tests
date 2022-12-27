from const import *


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple:
    check_arguments_for_validity(a, b, c)

    discriminant = b ** 2 - 4 * a * c
    if numbers_equal(discriminant, 0):
        return - b / 2 * a,

    if discriminant < 0:
        return ()

    return (-b + discriminant ** 0.5) / 2 * a, (-b - discriminant ** 0.5) / 2 * a


def check_arguments_for_validity(a, b, c):
    if check_iterable_for_infinite_or_nan_member([a, b, c]):
        raise ValueError(INFINITE_OR_NAN_PARAMETER_ERROR)

    if numbers_equal(a, 0):
        raise ValueError(ZERO_A_PARAMETER_ERROR_MSG)


def numbers_equal(compare_what: numeric, compare_with: numeric) -> bool:
    if abs(compare_what - compare_with) < FLOAT_ERROR_DELTA:
        return True
    return False


def check_iterable_for_infinite_or_nan_member(iterable_to_check):
    for value in iterable_to_check:
        if value != value:
            return True

        if value == float('inf') or value == float('-inf'):
            return True

    return False


if __name__ == '__main__':
    print(solve_quadratic_equation(1, 1, -2))

