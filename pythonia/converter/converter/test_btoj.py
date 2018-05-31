#Here is where we will implement the test.
from pytest import approx

# import the code to be tested
from converter import Calc

# write a smoke test
def test_smoke():
  assert True == True

# test conversion from Btu to J
def test_btuToJ():
  assert Calc.btuToJ(0) == 0
  assert Calc.btuToJ(100) == approx(105505.58526, abs=0.01)
  assert Calc.btuToJ(10) == approx(10550.558526, abs=0.01)
  assert Calc.btuToJ(-50) == 0
  assert Calc.btuToJ(22) == approx(23211.228758, abs=0.01)

# test conversion from J to Btu
def test_jtoBtu():
  assert Calc.jtoBtu(0) == 0
  assert Calc.jtoBtu(105505.58526) == approx(99.999999965, abs=0.01)
  assert Calc.jtoBtu(5000) == approx(4.7390856, abs=0.01)
  assert Calc.jtoBtu(23211.228758) == approx(22, abs=0.01)
  assert Calc.jtoBtu(5) == approx(0.0047390856, abs=0.01)
  assert Calc.jtoBtu(-50) == 0
