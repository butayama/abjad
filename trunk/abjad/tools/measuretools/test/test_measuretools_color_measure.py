from abjad import *


def test_measuretools_color_measure_01( ):

   measure = RigidMeasure((2, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(2))

   r'''
   {
        \time 2/8
        c'8
        d'8
   }
   '''

   measuretools.color_measure(measure, 'red')


   r'''
   {
        \override Beam #'color = #red
        \override Dots #'color = #red
        \override Staff.TimeSignature #'color = #red
        \override NoteHead #'color = #red
        \override Stem #'color = #red
        \time 2/8
        c'8
        d'8
        \revert Beam #'color
        \revert Dots #'color
        \revert Staff.TimeSignature #'color
        \revert NoteHead #'color
        \revert Stem #'color
   }
   '''

   assert check.wf(measure)
   assert measure.format == "{\n\t\\override Beam #'color = #red\n\t\\override Dots #'color = #red\n\t\\override Staff.TimeSignature #'color = #red\n\t\\override NoteHead #'color = #red\n\t\\override Stem #'color = #red\n\t\\time 2/8\n\tc'8\n\td'8\n\t\\revert Beam #'color\n\t\\revert Dots #'color\n\t\\revert Staff.TimeSignature #'color\n\t\\revert NoteHead #'color\n\t\\revert Stem #'color\n}"
