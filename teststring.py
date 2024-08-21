import Libcplx
import unittest

class TestStringMethods(unittest.TestCase):
  def test_cplxsum(self):
    suma=Libcplx.suma([3,2.8],[1.5,/-2])
    self.assertAlmostEqual(suma[0], 4.5)
    self.assertAlmostEqual(suma[1], 0.8)

  def test_cplxmulti(self):
    multi=Libcplx.multiplicacion([3,2.8],[1.5,/-2])
    self.assertAlmostEqual(multi[0], 10.1)
    self.assertAlmostEqual(multi[1], -1.8)

  def test_cplxdivi(self):
    divi=Libcplx.division([3,2.8],[1.5,/-2])
    self.assertAlmostEqual(divi[0], -0.2)
    self.assertAlmostEqual(divi[1], 1.6)

  def test_cplxresta(self):
    resta=Libcplx.resta([3,2.8],[1.5,/-2])
    self.assertAlmostEqual(resta[0], 1.5)
    self.assertAlmostEqual(resta[1], 4.8)

  def test_cplxmodulo(self):
    modulo=Libcplx.modulo([4,3])
    self.assertAlmostEqual(modulo, 5)

  def test_cplxconju(self):
    conju=Libcplx.conjugado([4,3])
    self.assertAlmostEqual(conju[0], 4)
    self.assertAlmostEqual(conju[1], -3)

  def test_cplxcatesiano(self):
    catesi=Libcplx.CVR([5,0.644],"catesiano")
    self.assertAlmostEqual(catesi[0], 4)
    self.assertAlmostEqual(catesi[1], 3)

  def test_cplxpolar(self):
    polar=Libcplx.CVR([4,3],"polar")
    self.assertAlmostEqual(polar[0], 5)
    self.assertAlmostEqual(polar[1], 0.6435011)
    
  def test_cplxphase(self):
    phase=Libcplx.fase([4,3])
    self.assertAlmostEqual(phase, 0.6435011)

if __name__=="__main__":
  unittest.main()
