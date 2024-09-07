import unittest
from maquinaPinceles import MaquinaHacerPinceles  

class TestMaquinaHacerPinceles(unittest.TestCase):

    def test_seleccionar_tipo_de_pelo(self):
        maquina = MaquinaHacerPinceles("nylon", 100, True)
        maquina.seleccionar_tipo_de_pelo("sintetico")
        self.assertEqual(maquina.tipo_pelo, "sintetico")  # Verifica que el tipo de pelo haya cambiado

    def test_ensamblar_pincel(self):
        maquina = MaquinaHacerPinceles("nylon", 100, True)
        maquina.ensamblar_pincel(True)  
        self.assertGreater(maquina.produccion_total, 0)  # Verifica que la producción sea mayor que 0

    def test_calcular_costo_produccion(self):
        maquina = MaquinaHacerPinceles("nylon", 100, True)
        maquina.produccion_total = 5  # Se Asigna un valor de producción para probar
        costo = maquina.calcular_costo_produccion(2)
        self.assertEqual(costo, 10)  # Verifica que el costo se calcule correctamente


if __name__ == "__main__":
    unittest.main()