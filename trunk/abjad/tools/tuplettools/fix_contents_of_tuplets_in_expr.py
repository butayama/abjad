from abjad.leaf import _Leaf
from abjad.rational import Rational
from abjad.tools import leaftools
from abjad.tuplet import FixedDurationTuplet
from abjad.tuplet import FixedMultiplierTuplet
import math


def fix_contents_of_tuplets_in_expr(tuplet):
   '''Scale `tuplet` contents by power of two
   if tuplet multiplier less than 1/2 or greater than 2.
   Return tuplet. ::

      abjad> tuplet = FixedDurationTuplet((2, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3, Rational(1, 4)))
      abjad> tuplet   
      FixedDurationTuplet(1/4, [c'4, d'4, e'4])
      abjad> tuplettools.fix_contents_of_tuplets_in_expr(tuplet)
      FixedDurationTuplet(1/4, [c'8, d'8, e'8])

   .. versionchanged:: 1.1.2
      renamed ``tuplettools.contents_fix( )`` to
      ``tuplettools.fix_contents_of_tuplets_in_expr( )``.
   '''

   # check input
   if isinstance(tuplet, FixedMultiplierTuplet):
      raise NotImplemented
   elif not isinstance(tuplet, FixedDurationTuplet):
      raise ValueError('must be tuplet.')

   # find tuplet multiplier
   integer_exponent = int(math.log(tuplet.duration.multiplier, 2))
   leaf_multiplier = Rational(2) ** integer_exponent

   # scale leaves in tuplet by power of two
   for component in tuplet[:]:
      if isinstance(component, _Leaf):
         old_written_duration = component.duration.written
         new_written_duration = leaf_multiplier * old_written_duration
         leaftools.change_leaf_preprolated_duration(
            component, new_written_duration)

   return tuplet
