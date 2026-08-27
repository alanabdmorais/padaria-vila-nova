import unittest

from padaria import calcular_total


class TestCalcularTotal(unittest.TestCase):
    def test_multiplica_preco_por_quantidade(self):
        self.assertEqual(calcular_total(5.0, 3), 15.0)

    def test_quantidade_zero_retorna_zero(self):
        self.assertEqual(calcular_total(4.5, 0), 0)

    def test_arredonda_para_duas_casas_decimais(self):
        self.assertEqual(calcular_total(0.1, 3), 0.3)

    def test_valores_negativos_geram_erro(self):
        with self.assertRaises(ValueError):
            calcular_total(-1, 2)


if __name__ == "__main__":
    unittest.main()
