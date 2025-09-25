import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from drivers.test_driver import TestDriver
from nomina_sistema import NominaSistema

class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()
        self.driver = TestDriver(self.calc)

    def test_isr_salario_bajo(self):
        salario = 8000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        resultado = self.calc.calcular_isr(15000)
        assert resultado == 1500  # 10% de 15000

    def test_seguro_social(self):
        resultado = self.calc.calcular_seguro_social(10000)
        assert resultado == 625  # 6.25% de 10000


class TestIntegracion:
    """Nivel 2: Prueba sistema integrado"""

    def setup_method(self):
        self.nomina = NominaSistema()

    def test_nomina_simple(self):
        empleado = {
            "salario_base": 10000,
            "bono": 500,
            "deducciones": 200
        }
        neto = self.nomina.calcular_nomina_neta(empleado)
        # 10000 + 500 - ISR(500) - Seguro(625) - Deducciones(200)
        assert neto == 9175
