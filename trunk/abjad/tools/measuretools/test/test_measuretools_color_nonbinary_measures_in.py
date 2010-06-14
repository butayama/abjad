from abjad import *


def test_measuretools_color_nonbinary_measures_in_01( ):

   staff = Staff(RigidMeasure((2, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(2)) * 2)
   measuretools.change_binary_measure_to_nonbinary(staff[1], 3)

   r'''
   \new Staff {
        {
                \time 2/8
                c'8
                d'8
        }
        {
                \time 3/12
                \scaleDurations #'(2 . 3) {
                        c'8.
                        d'8.
                }
        }
   }
   '''

   measuretools.color_nonbinary_measures_in(staff, 'red')


   r'''
   \new Staff {
        {
                \time 2/8
                c'8
                d'8
        }
        {
                \override Beam #'color = #red
                \override Dots #'color = #red
                \override Staff.TimeSignature #'color = #red
                \override NoteHead #'color = #red
                \override Stem #'color = #red
                \time 3/12
                \scaleDurations #'(2 . 3) {
                        c'8.
                        d'8.
                }
                \revert Beam #'color
                \revert Dots #'color
                \revert Staff.TimeSignature #'color
                \revert NoteHead #'color
                \revert Stem #'color
        }
   }
   '''

   assert check.wf(staff)
   assert staff.format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8\n\t\td'8\n\t}\n\t{\n\t\t\\override Beam #'color = #red\n\t\t\\override Dots #'color = #red\n\t\t\\override Staff.TimeSignature #'color = #red\n\t\t\\override NoteHead #'color = #red\n\t\t\\override Stem #'color = #red\n\t\t\\time 3/12\n\t\t\\scaleDurations #'(2 . 3) {\n\t\t\tc'8.\n\t\t\td'8.\n\t\t}\n\t\t\\revert Beam #'color\n\t\t\\revert Dots #'color\n\t\t\\revert Staff.TimeSignature #'color\n\t\t\\revert NoteHead #'color\n\t\t\\revert Stem #'color\n\t}\n}"
