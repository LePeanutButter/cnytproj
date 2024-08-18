import Libcplx as lc
import unittest
import math

class TestStringMethods(unittest.TestCase):
    def test_suma1(self): # (2+3i)+(-1+4i) = 1+7i
        suma = lc.sumaC([2,3],[-1,4])
        self.assertAlmostEqual(suma[0], 1)
        self.assertAlmostEqual(suma[1], 7)

    def test_suma2(self): # (3+4i)+7i = 3+11i
        suma = lc.sumaC([3,4],[0,7])
        self.assertAlmostEqual(suma[0], 3)
        self.assertAlmostEqual(suma[1], 11)
    
    def test_resta1(self): # (4+4√3i)-(-√2+i) = 5.4142+5.9282i
        resta = lc.restaC((4,4*math.sqrt(3)),(-math.sqrt(2),1))
        self.assertAlmostEqual(resta[0], 5.4142)
        self.assertAlmostEqual(resta[1], 5.9282)

    def test_resta2(self): # (8+√11i)-(3+4i) = 5-0.6834i
        resta = lc.restaC((8,math.sqrt(11)),(3,4))
        self.assertAlmostEqual(resta[0], 5)
        self.assertAlmostEqual(resta[1], -0.6834)

    def test_multiplicacion1(self): # (2+3i)**2 = -5+12i
        multiplicacion = lc.multiplicacionC([2,3],[2,3])
        self.assertAlmostEqual(multiplicacion[0], -5)
        self.assertAlmostEqual(multiplicacion[1], 12)

    def test_multiplicacion2(self): # (-2-i)*(-1-2i) = 5i
        multiplicacion = lc.multiplicacionC([-2,-1],[-1,-2])
        self.assertAlmostEqual(multiplicacion[0], 0)
        self.assertAlmostEqual(multiplicacion[1], 5)
    
    def test_division1(self): # i/(3-2i) = -0.1538+0.2308i
        division = lc.divisionC([0,1],[3,-2])
        self.assertAlmostEqual(division[0], -0.1538)
        self.assertAlmostEqual(division[1], 0.2308)

    def test_division2(self): # (20+30i)/(3+i) = 9+7i
        division = lc.divisionC([20,30],[3,1])
        self.assertAlmostEqual(division[0], 9)
        self.assertAlmostEqual(division[1], 7)
    
    def test_modulo1(self): # |(19/2)-(3/4)i| = 9.5296
        modulo = lc.moduloC([(19/2),(-3/4)])
        self.assertAlmostEqual(modulo, 9.5296)

    def test_modulo2(self): # |3+(5/2)i| = 3.9051
        modulo = lc.moduloC([3,(5/2)])
        self.assertAlmostEqual(modulo, 3.9051)
    
    def test_conjugado1(self): # 4+3i = 4-3i
        conjugado = lc.conjugadoC([4,3])
        self.assertAlmostEqual(conjugado[0], 4)
        self.assertAlmostEqual(conjugado[1], -3)

    def test_conjugado2(self): # -2-5i = -2+5i
        conjugado = lc.conjugadoC([-2,-5])
        self.assertAlmostEqual(conjugado[0], -2)
        self.assertAlmostEqual(conjugado[1], 5)
    
    def test_cartesiano(self): # ρ=3 ^ θ=(π/3)rad => 1.5+2.5981i
        cartesiano = lc.CVR([3,(math.pi/3)], "cartesiano")
        self.assertAlmostEqual(cartesiano[0], 1.5)
        self.assertAlmostEqual(cartesiano[1], 2.5981)

    def test_polar(self): # -1+3i => ρ=3.1623 ^ θ=-1.2490rad
        polar = lc.CVR([-1,3], "polar")
        self.assertAlmostEqual(polar[0], 3.1623)
        self.assertAlmostEqual(polar[1], -1.2490)
    
    def test_fase1(self): # 3+5i => θ=1.0304rad
        fase = lc.fase([3,5])
        self.assertAlmostEqual(fase, 1.0304)

    def test_fase2(self): # (-1/2)+(√3/2)i => θ=-1.0472rad
        fase = lc.fase([(-1/2),((math.sqrt(3))/2)])
        self.assertAlmostEqual(fase, -1.0472)

if __name__ == "__main__":
    unittest.main()