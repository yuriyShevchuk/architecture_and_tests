import unittest

from small_tasks.quadratic_equation import solve_quadratic_equation


class EquationTestCase(unittest.TestCase):
    def test_solve_quadratic_equation_a_is_zero(self):
        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(0.000_000_001, 1, 1)
        self.assertEqual(str(exception_context.exception), "Zero parameter A in equation")

    def test_solve_quadratic_equation_no_solutions(self):
        actual = solve_quadratic_equation(1, 1, 1)
        self.assertEqual(actual, ())


if __name__ == '__main__':
    unittest.main()
