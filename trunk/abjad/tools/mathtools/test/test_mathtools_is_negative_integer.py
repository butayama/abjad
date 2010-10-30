from abjad import *


def test_mathtools_is_negative_integer_01( ):

   assert not mathtools.is_negative_integer(1)
   assert not mathtools.is_negative_integer(long(1))
   assert not mathtools.is_negative_integer(Fraction(1, 1))
   assert not mathtools.is_negative_integer(1.0)
   assert not mathtools.is_negative_integer(True)
   assert not mathtools.is_negative_integer(0)
   assert not mathtools.is_negative_integer(False)
   

def test_mathtools_is_negative_integer_02( ):
 
   assert mathtools.is_negative_integer(-99)


def test_mathtools_is_negative_integer_03( ):

   assert not mathtools.is_negative_integer('foo')
