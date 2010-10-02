from abjad import *


def test_Chord___contains___01( ):

   chord = Chord([3, 13, 17], (1, 4))

   assert 17 in chord
   assert 17.0 in chord
   assert pitchtools.NamedPitch(17) in chord
   assert pitchtools.NamedPitch("f''") in chord
   assert chord[1] in chord
   assert not notetools.NoteHead("f''") in chord


def test_Chord___contains___02( ):

   chord = Chord([3, 13, 17], (1, 4))

   assert not 18 in chord
   assert not 18.0 in chord
   assert not pitchtools.NamedPitch(18) in chord
   assert not pitchtools.NamedPitch("fs''") in chord
   assert not notetools.NoteHead(18) in chord
   assert not notetools.NoteHead("fs''") in chord
