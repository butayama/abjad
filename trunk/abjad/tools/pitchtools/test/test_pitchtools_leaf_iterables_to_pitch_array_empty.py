from abjad import *


def test_pitchtools_leaf_iterables_to_pitch_array_empty_01( ):

   score = Score([ ])
   score.append(Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(6)))
   score.append(Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3, Rational(1, 4))))
   score.append(Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(6)))

   r'''
   \new Score <<
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
                   g'8
                   a'8
           }
           \new Staff {
                   c'4
                   d'4
                   e'4
           }
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
                   g'8
                   a'8
           }
   >>
   '''

   pitch_array = pitchtools.leaf_iterables_to_pitch_array_empty(score)

   '''
   [ ] [ ] [ ] [ ] [ ] [ ]
   [     ] [     ] [     ]
   [ ] [ ] [ ] [ ] [ ] [ ]
   '''

   assert pitch_array[0].cell_widths == (1, 1, 1, 1, 1, 1)
   assert pitch_array[1].cell_widths == (2, 2, 2)
   assert pitch_array[2].cell_widths == (1, 1, 1, 1, 1, 1)


def test_pitchtools_leaf_iterables_to_pitch_array_empty_02( ):

   score = Score([ ])
   score.append(Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(4)))
   score.append(Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(2, Rational(1, 4))))
   score.append(Staff(FixedDurationTuplet((2, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(3)) * 2))

   r'''
   \new Score <<
           \new Staff {
                   c'8
                   d'8
                   e'8
                   f'8
           }
           \new Staff {
                   c'4
                   d'4
           }
           \new Staff {
                   \times 2/3 {
                           c'8
                           d'8
                           e'8
                   }
                   \times 2/3 {
                           c'8
                           d'8
                           e'8
                   }
           }
   >>
   '''

   pitch_array = pitchtools.leaf_iterables_to_pitch_array_empty(score)

   '''
   [     ] [     ] [     ] [     ]
   [             ] [             ]
   [ ] [     ] [ ] [ ] [     ] [ ]
   '''

   assert pitch_array[0].cell_widths == (2, 2, 2, 2)
   assert pitch_array[1].cell_widths == (4, 4)
   assert pitch_array[2].cell_widths == (1, 2, 1, 1, 2, 1)
