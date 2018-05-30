#Here is where we will implement the test.
from pytest import approx

# import the code to be tested
from converter import btuToJ, jtoBtu

# write a smoke test
def test_smoke():
  assert True == True

# test conversion from Btu to J
def test_btuToJ():
  assert btuToJ(0) == 0
  assert btuToJ(100) == approx(105505.58526, abs=0.01)
  assert btuToJ(10) == approx(10550.558526, abs=0.01)
  assert btuToJ(22) == approx(23211.228758, abs=0.01)
  assert btuToJ(-10) == approx(-10550.558526, abs=0.01)
  assert btuToJ(-20) == approx(-21101.117052, abs=0.01)
  assert btuToJ(-17.78) == approx(-18758.89306, abs=0.01)

# test conversion from J to Btu
def test_jtoBtu():
  assert jtoBtu(0) == 0
  assert jtoBtu(105505.58526) == approx(99.999999965, abs=0.01)
  assert jtoBtu(5000) == approx(4.7390856, abs=0.01)
  assert jtoBtu(23211.228758) == approx(22, abs=0.01)
  assert jtoBtu(5) == approx(0.0047390856, abs=0.01)
  assert jtoBtu(15) == approx(0.0142172568, abs=0.01)
  assert jtoBtu(-17.78) == approx(-0.016852188394, abs=0.01)