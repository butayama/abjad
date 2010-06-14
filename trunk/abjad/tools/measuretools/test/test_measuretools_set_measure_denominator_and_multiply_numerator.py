from abjad import *


def test_measuretools_set_measure_denominator_and_multiply_numerator_01( ):

   t = RigidMeasure((3, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
   measuretools.set_measure_denominator_and_multiply_numerator(t, 16)

   r'''
   {
           \time 6/16
           c'8
           d'8
           e'8
   }
   '''

   assert check.wf(t)
   assert t.format == "{\n\t\\time 6/16\n\tc'8\n\td'8\n\te'8\n}"

   measuretools.set_measure_denominator_and_multiply_numerator(t, 8)

   r'''
   {
           \time 3/8
           c'8
           d'8
           e'8
   }
   '''

   assert check.wf(t)
   assert t.format == "{\n\t\\time 3/8\n\tc'8\n\td'8\n\te'8\n}"
