import unittest

from small_tasks.quadratic_equation import solve_quadratic_equation


class EquationTestCase(unittest.TestCase):
    def test_solve_quadratic_equation_a_zero(self):
        with self.assertRaises(ValueError) as exception_context:
            solve_quadratic_equation(0.000000001, 1, 1)
        self.assertEqual(str(exception_context.exception), "Zero parameter A in equation")


if __name__ == '__main__':
    unittest.main()
