from abjad import *

def test_fuse_tied_leaves_by_prolated_durations_01( ):
   '''Tied leaves inside containers can be fused.''' 

   t = Voice(leaftools.make_repeated_notes(4))
   tie = Tie(t.leaves)
   fuse.tied_leaves_by_prolated_durations(t.leaves, [Rational(1, 4)])

   r'''
   \new Voice {
        c'4 ~
        c'8 ~
        c'8
   }
   '''

   assert len(t) == 3
   assert t[0].duration.prolated == Rational(1, 4)
   assert t[1].duration.prolated == Rational(1, 8)
   assert t[2].duration.prolated == Rational(1, 8)
   assert t[0] in tie
   assert t[1] in tie
   assert t[2] in tie

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\tc'4 ~\n\tc'8 ~\n\tc'8\n}"


def test_fuse_tied_leaves_by_prolated_durations_02( ):
   '''Tied leaves inside containers can be fused.''' 

   t = Voice(leaftools.make_repeated_notes(4))
   tie = Tie(t.leaves[1:])
   fuse.tied_leaves_by_prolated_durations(t.leaves, [Rational(1, 4)])

   r'''
   \new Voice {
           c'8
           c'8 ~
           c'8 ~
           c'8
   }
   '''

   assert len(t) == 4
   assert t[0].duration.prolated == Rational(1, 8)
   assert t[1].duration.prolated == Rational(1, 8)
   assert t[2].duration.prolated == Rational(1, 8)
   assert t[3].duration.prolated == Rational(1, 8)
   assert t[0] not in tie
   assert t[1] in tie
   assert t[2] in tie
   assert t[3] in tie

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\tc'8\n\tc'8 ~\n\tc'8 ~\n\tc'8\n}"


def test_fuse_tied_leaves_by_prolated_durations_03( ):
   '''multiple ties inside the same duration span are independently fused.''' 

   t = Voice(leaftools.make_repeated_notes(4))
   tie1 = Tie(t.leaves[0:2])
   tie2 = Tie(t.leaves[2:])
   fuse.tied_leaves_by_prolated_durations(t.leaves, [Rational(1, 4)] * 2)

   r'''
   \new Voice {
        c'4
        c'4
   }
   '''

   assert len(t) == 2
   assert t[0].duration.prolated == Rational(1, 4)
   assert t[1].duration.prolated == Rational(1, 4)
   assert t[0] in tie1
   assert t[1] in tie2

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\tc'4\n\tc'4\n}"


def test_fuse_tied_leaves_by_prolated_durations_04( ):
   '''multiple ties inside the same duration span are independently fused.''' 

   t = Voice(leaftools.make_repeated_notes(8))
   Tie(t.leaves[0:4])
   Tie(t.leaves[4:])

   r'''
   \new Voice {
           c'8 ~
           c'8 ~
           c'8 ~
           c'8
           c'8 ~
           c'8 ~
           c'8 ~
           c'8
   }
   '''

   fuse.tied_leaves_by_prolated_durations(t.leaves[1:-1], [Rational(1, 4)] * 3)

   r'''
   \new Voice {
           c'8 ~
           c'4 ~
           c'8
           c'8 ~
           c'4 ~
           c'8
   } 
   '''

   assert t.format == "\\new Voice {\n\tc'8 ~\n\tc'4 ~\n\tc'8\n\tc'8 ~\n\tc'4 ~\n\tc'8\n}"


def test_fuse_tied_leaves_by_prolated_durations_05( ):
   '''Steve Lehman's "Rai" slicing example.'''
   durations = [5, 7, 2, 11, 13, 5, 13, 3]
   durations = zip(durations, [16] * len(durations))

   notes = leaftools.make_notes(0, durations)
   t = RhythmicSketchStaff(notes)

   meters = [(1, 4)] * 4 + [(2, 4)] + [(1, 4)] * 6 + [(2, 4)] + [(3, 16)]
   meters = durtools.rationalize(meters)

   partition.unfractured_by_durations(t.leaves, meters, tie_after=True)

   r'''
   \new RhythmicStaff \with {
           \override BarLine #'transparent = ##t
           \override TimeSignature #'transparent = ##t
   } {
           c'4 ~
           c'16
           c'8. ~
           c'4
           c'8
           c'8 ~
           c'4. ~
           c'8 ~
           c'16
           c'8. ~
           c'4 ~
           c'4 ~
           c'16 ~
           c'16
           c'8 ~
           c'8 ~
           c'16
           c'16 ~
           c'4 ~
           c'4 ~
           c'8. ~
           c'16
           c'8.
   }
   '''

   fuse.tied_leaves_by_prolated_durations(t.leaves, meters)

   check.wf(t, runtime='format')
   assert t.format == "\\new RhythmicStaff \\with {\n\t\\override BarLine #'transparent = ##t\n\t\\override TimeSignature #'transparent = ##t\n} {\n\tc'4 ~\n\tc'16\n\tc'8. ~\n\tc'4\n\tc'8\n\tc'8 ~\n\tc'2 ~\n\tc'16\n\tc'8. ~\n\tc'4 ~\n\tc'4 ~\n\tc'8\n\tc'8 ~\n\tc'8.\n\tc'16 ~\n\tc'4 ~\n\tc'2\n\tc'8.\n}"


   r'''
      \new RhythmicStaff \with {
           \override BarLine #'transparent = ##t
           \override TimeSignature #'transparent = ##t
   } {
           c'4 ~
           c'16
           c'8. ~
           c'4
           c'8
           c'8 ~
           c'2 ~
           c'16
           c'8. ~
           c'4 ~
           c'4 ~
           c'8
           c'8 ~
           c'8.
           c'16 ~
           c'4 ~
           c'2
           c'8.
   }
   '''
