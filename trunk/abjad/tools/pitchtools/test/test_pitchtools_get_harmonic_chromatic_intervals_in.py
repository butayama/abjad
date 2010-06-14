from abjad import *


def test_pitchtools_get_harmonic_chromatic_intervals_in_01( ):

   staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(4))

   intervals = pitchtools.get_harmonic_chromatic_intervals_in(staff)
   intervals = sorted(list(intervals))
   numbers = [hci.number for hci in intervals]

   assert numbers == [1, 2, 2, 3, 4, 5]
