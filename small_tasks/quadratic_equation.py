from const import FLOAT_ERROR_DELTA, numeric


def numbers_equal(compare_what: numeric, compare_with: numeric) -> bool:
    if abs(compare_what - compare_with) < FLOAT_ERROR_DELTA:
        return True
    return False


def solve_quadratic_equation(a: float, b: float, c: float):
    if numbers_equal(a, 0):
        raise ValueError("Zero parameter A in equation")
