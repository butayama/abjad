from abjad import *


def test_leaftools_divide_leaves_meiotically_in_01( ):
   '''Meiose each leaf in two.'''

   t = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   Beam(t[:])
   leaftools.divide_leaves_meiotically_in(t)

   r'''
   \new Voice {
      c'16 [
      c'16
      d'16
      d'16
      e'16
      e'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\tc'16 [\n\tc'16\n\td'16\n\td'16\n\te'16\n\te'16 ]\n}"


def test_leaftools_divide_leaves_meiotically_in_02( ):
   '''Meiose one leaf in four.'''

   t = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   Beam(t[:])
   leaftools.divide_leaves_meiotically_in(t[0], 4)

   r'''
   \new Voice {
      c'32 [
      c'32
      c'32
      c'32
      d'8
      e'8 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\tc'32 [\n\tc'32\n\tc'32\n\tc'32\n\td'8\n\te'8 ]\n}"
