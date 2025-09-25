class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""

    def calcular_bonos(self, empleado):
        """Devuelve el bono asignado al empleado"""
        return empleado.get('bono', 0)
