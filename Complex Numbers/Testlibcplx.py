import Libcplx as lc
import unittest

class TestStringMethods(unittest.TestCase):
    def test_cplxsum(self):
        suma= lc.sumaC([3,2.8],[1.5,-2])
        self.assertAlmostEqual(suma[0], 4.5)
        self.assertAlmostEqual(suma[1], 0.8)

    def test_cplxmult(self):
        mult= lc.multiplicacionC([3,2.8],[1.5,-2])
        self.assertAlmostEqual(mult[0], 10.1)
        self.assertAlmostEqual(mult[1], -1.8)
    
    def test_cplxdiv(self):
        div= lc.divisionC([3,2.8],[1.5,-2])
        self.assertAlmostEqual(div[0], -0.2)
        self.assertAlmostEqual(div[1], 1.6)
    
    def test_cplxresta(self):
        resta= lc.restaC((3,2.8),(1.5,-2))
        self.assertAlmostEqual(resta[0], 1.5)
        self.assertAlmostEqual(resta[1], 4.8)
    
    def test_cplxmodulo(self):
        modulo= lc.moduloC([4,3])
        self.assertAlmostEqual(modulo, 5)
    
    def test_clpxconjugado(self):
        conj=lc.conjugadoC([4,3])
        self.assertAlmostEqual(conj[0], 4)
        self.assertAlmostEqual(conj[1], -3)
    
    def test_clpxpolar(self):
        polar=lc.CVR([4,3], "polar")
        self.assertAlmostEqual(polar[0], 5)
        self.assertAlmostEqual(polar[1], 0.6435011)
        
    def test_clpxcartesiana(self):
        cart=lc.CVR([5,0.644], "cartesiano")
        self.assertAlmostEqual(cart[0], 4)
        self.assertAlmostEqual(cart[1], 3)
    
    def test_clpxphase(self):
        phase=lc.fase([4,3])
        self.assertAlmostEqual(phase, 0.6435011)

if __name__ == "__main__":
    unittest.main()