import unittest

from small_tasks.quadratic_equation import solve_quadratic_equation
from const import *


class EquationTestCase(unittest.TestCase):
    def test_solve_quadratic_equation_a_is_zero(self):
        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(0.000_000_000_000_000_1, 1, 1)
        self.assertEqual(str(exception_context.exception), ZERO_A_PARAMETER_ERROR_MSG)

    def test_solve_quadratic_equation_no_solutions(self):
        actual = solve_quadratic_equation(1, 1, 1)
        self.assertEqual(actual, ())

    def test_solve_quadratic_equation_one_solution(self):
        actual = solve_quadratic_equation(1, 2, 0.999_999_999_999_999_9)
        self.assertEqual(actual, (-1.0,))

    def test_solve_quadratic_equation_two_solutions(self):
        actual = solve_quadratic_equation(1, 1, -2)
        self.assertEqual(actual, (1.0, -2.0))

    def test_solve_quadratic_equation_right_return_type(self):
        self.assertIsInstance(solve_quadratic_equation(2, 4, 2), tuple)
        self.assertIsInstance(solve_quadratic_equation(1, 1, -2), tuple)
        self.assertIsInstance(solve_quadratic_equation(1, 1, 1), tuple)

    def test_solve_quadratic_equation_check_for_inf(self):
        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(float('inf'), 1, 1)
        self.assertEqual(str(exception_context.exception), INFINITE_OR_NAN_PARAMETER_ERROR)

        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(1, float('-inf'), 1)
        self.assertEqual(str(exception_context.exception), INFINITE_OR_NAN_PARAMETER_ERROR)

        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(1, 1, float('inf'))
        self.assertEqual(str(exception_context.exception), INFINITE_OR_NAN_PARAMETER_ERROR)

        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(1, 1, float('nan'))
        self.assertEqual(str(exception_context.exception), INFINITE_OR_NAN_PARAMETER_ERROR)


if __name__ == '__main__':
    unittest.main()
