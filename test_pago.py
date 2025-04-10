import unittest
from pago import calcular_pago

class TestPago(unittest.TestCase):
        
    def test1(self):
        contrato = "tiempo completo"
        horas_diurnas = 40
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)
        
        self.assertAlmostEqual(1900.0, calcular_pagos, places=2)

    def test2(self):
        contrato = "medio tiempo"
        horas_diurnas = 20
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(570.0, calcular_pagos, places=2)

    def test3(self):
        contrato = "tiempo completo"
        horas_diurnas = 30
        horas_nocturnas = 10
        horas_dominicales = 0
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(2327.5, calcular_pagos, places=2)

    def test4(self):
        contrato = "tiempo completo"
        horas_diurnas = 35
        horas_nocturnas = 0
        horas_dominicales = 5
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(2175.0, calcular_pagos, places=2)

    def test5(self):
        contrato = "tiempo completo"
        horas_diurnas = 30
        horas_nocturnas = 5
        horas_dominicales = 5
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(2388.75125, calcular_pagos, places=2)

    def test6(self):
        contrato = "freelance"
        horas_diurnas = 0
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        with self.assertRaises(ValueError):
            calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

    def test7(self):
        contrato = "tiempo completo"
        horas_diurnas = -10
        horas_nocturnas = -10
        horas_dominicales = -10
        horas_festivas = -10

        with self.assertRaises(ValueError):
            calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

    def test8(self):
        contrato = "tiempo completo"
        horas_diurnas = "A"
        horas_nocturnas = "B"
        horas_dominicales = "C"
        horas_festivas = "D"

        with self.assertRaises(TypeError):
            calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

    def test9(self):
        contrato = "tiempo completo"
        horas_diurnas = 4.5
        horas_nocturnas = 4.5
        horas_dominicales = 4.5
        horas_festivas = 4.5

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(1378.2386250000002, calcular_pagos, places=2)

    def test10(self):
        contrato = ""
        with self.assertRaises(TypeError):
            calcular_pago(contrato, None, None, None, None)

    def test11(self):
        contrato = "medio tiempo"
        horas_diurnas = 10
        horas_nocturnas = 5
        horas_dominicales = 0
        horas_festivas = 5

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(902.91135, calcular_pagos, places=2)

    def test12(self):
        contrato = "tiempo completo"
        horas_diurnas = 0
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(0.0, calcular_pagos, places=2)

    def test13(self):
        contrato = "medio tiempo"
        horas_diurnas = 50
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(1425.0, calcular_pagos, places=2)

    def test14(self):
        contrato = "tiempo completo"
        horas_diurnas = 1000
        horas_nocturnas = 1000
        horas_dominicales = 1000
        horas_festivas = 1000

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(306275.25, calcular_pagos, places=2)
        
        
    def test15(self):
        contrato = "tiempo completo"
        horas_diurnas = 1
        horas_nocturnas = 1
        horas_dominicales = 1
        horas_festivas = 1

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(306.27524999999997, calcular_pagos, places=2)

    def test16(self):
        contrato = "tiempo completo"
        horas_diurnas = "@"
        horas_nocturnas = "#"
        horas_dominicales = "&"
        horas_festivas = "%"

        with self.assertRaises(TypeError):
            calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

    def test17(self):
        contrato = "medio tiempo"
        horas_diurnas = 1000
        horas_nocturnas = 1000
        horas_dominicales = 1000
        horas_festivas = 1000

        calcular_pagos = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)

        self.assertAlmostEqual(233139.4677, calcular_pagos, places=2)

    def test18(self):
        contrato = "tiempo completo"
        horas_diurnas = 40
        horas_nocturnas = 0
        horas_dominicales = 0
        horas_festivas = 0

        pago_neto = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)
        descuento_parafiscales = pago_neto * 0.05

        self.assertAlmostEqual(descuento_parafiscales, 95.0, places=2)

    def test19(self):
        contrato = "medio tiempo"
        horas_diurnas = 30
        horas_nocturnas = 10
        horas_dominicales = 5
        horas_festivas = 5

        pago_neto = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)
        descuento_parafiscales = pago_neto * 0.05

        self.assertTrue(descuento_parafiscales >= 0 and descuento_parafiscales <= pago_neto)

    def test20(self):
        contrato = "medio tiempo"
        horas_diurnas = 25
        horas_nocturnas = 5
        horas_dominicales = 5
        horas_festivas = 5

        pago_neto = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)
        descuento_parafiscales = pago_neto * 0.05

        self.assertAlmostEqual(pago_neto + descuento_parafiscales, 1822.4822054250003, places=2)



if __name__ == '__main__':
    unittest.main()
