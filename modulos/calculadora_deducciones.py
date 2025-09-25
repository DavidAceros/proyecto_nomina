class CalculadoraDeducciones:
    """Módulo base para cálculo de deducciones adicionales"""

    def calcular_deducciones(self, empleado):
        """Calcula las deducciones según el empleado"""
        return empleado.get("deducciones", 0)
