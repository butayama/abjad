from abjad.rational import Rational
import math


def naive_prolated_to_written_not_less_than(prolated_duration):
   '''Return the least rational of the form ``1/2**n`` 
   greater than or equal to `prolated_duration`. ::

      abjad> for n in range(1, 17):
      ...     prolated_duration = Rational(n, 16)
      ...     written_duration = durtools.naive_prolated_to_written_not_less_than(prolated_duration)
      ...     print '%s/16\\t%s' % (n, written_duration)
      ... 
      1/16    1/16
      2/16    1/8
      3/16    1/4
      4/16    1/4
      5/16    1/2
      6/16    1/2
      7/16    1/2
      8/16    1/2
      9/16    1
      10/16   1
      11/16   1
      12/16   1
      13/16   1
      14/16   1
      15/16   1
      16/16   1

   ::

      abjad> durtools.naive_prolated_to_written_not_less_than(Rational(1, 80))
      Rational(1, 64)

   Function intended to find written duration of notes inside tuplet.
   '''

   # find exponent of denominator
   exponent = -int(math.ceil(math.log(prolated_duration, 2)))

   # find numerator, denominator and written duration
   numerator = 1
   denominator = 2 ** exponent
   written_duration = Rational(numerator, denominator)

   # return written duration
   return written_duration
