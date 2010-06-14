from abjad import *


def test_pitchtools_expr_to_melodic_chromatic_interval_segment_01( ):

   staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(8))
   mciseg = pitchtools.expr_to_melodic_chromatic_interval_segment(staff)

   assert mciseg.melodic_chromatic_interval_numbers == (2, 2, 1, 2, 2, 2, 1)
