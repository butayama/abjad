from abjad import *


def test_TextSpannerInterface_spanner_reception_01( ):

   t = Staff(macros.scale(4))
   text_spanner = spannertools.TextSpanner(t[:])

   r'''
   \new Staff {
           c'8 \startTextSpan
           d'8
           e'8
           f'8 \stopTextSpan
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t[0].text_spanner.spanner is text_spanner
