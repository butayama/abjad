from abjad import *


def test_measuretools_apply_beam_spanners_to_measures_in( ):
   '''Beam all measures in expr with plain old Beam spanner.'''

   staff = Staff(RigidMeasure((2, 8), leaftools.make_repeated_notes(2)) * 2)
   pitchtools.diatonicize(staff)

   r'''
   \new Staff {
        {
                \time 2/8
                c'8
                d'8
        }
        {
                \time 2/8
                e'8
                f'8
        }
   }
   '''

   measuretools.apply_beam_spanners_to_measures_in(staff)


   r'''
   \new Staff {
        {
                \time 2/8
                c'8 [
                d'8 ]
        }
        {
                \time 2/8
                e'8 [
                f'8 ]
        }
   }
   '''

   assert check.wf(staff)
   assert staff.format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8 [\n\t\td'8 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ]\n\t}\n}"
