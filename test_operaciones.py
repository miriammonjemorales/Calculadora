import unittest
from math_operations import sumar, restar, multiplicar, dividir

class TestMathOperations(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(0, 1), -1)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, -3), 2)
        with self.assertRaises(ValueError):
            dividir(5, 0)

    # Pruebas adicionales
    def test_invalid_inputs(self):
        for func in [sumar, restar, multiplicar, dividir]:
            with self.assertRaises(TypeError):
                func(None, 3)
            with self.assertRaises(TypeError):
                func(3, None)
            with self.assertRaises(TypeError):
                func([], {})
            with self.assertRaises(TypeError):
                func("string", [1, 2, 3])

    def test_dividir_edge_cases(self):
        self.assertEqual(dividir(0, 5), 0)  # Dividir 0 por un número
        with self.assertRaises(ValueError):  # Dividir 0 entre 0
            dividir(0, 0)

    def test_large_numbers(self):
        self.assertEqual(multiplicar(1e10, 1e10), 1e20)
        self.assertEqual(dividir(1e20, 1e10), 1e10)
        self.assertEqual(restar(1e20, 1e20), 0)
        self.assertEqual(sumar(1e20, -1e20), 0)

if __name__ == "__main__":
    unittest.main()
