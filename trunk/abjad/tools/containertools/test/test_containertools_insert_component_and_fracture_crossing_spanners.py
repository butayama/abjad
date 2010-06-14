from abjad import *


def test_containertools_insert_component_and_fracture_crossing_spanners_01( ):
   '''Insert component into container at index i.      
      Fracture spanners to the left of index i.
      Fracture spanners to the right of index i.      
      Return Python list of fractured spanners.'''

   "Insert works just before a spanner."

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, 0, Rest((1, 4)))

   r'''
   \new Staff {
           r4
           c'8 [
           cs'8
           d'8
           ef'8 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tr4\n\tc'8 [\n\tcs'8\n\td'8\n\tef'8 ]\n}"   
   
def test_containertools_insert_component_and_fracture_crossing_spanners_02( ):
   '''Insert works inside a spanner.'''

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, 1, Rest((1, 4)))

   r'''
   \new Staff {
           c'8 [ ]
           r4
           cs'8 [
           d'8
           ef'8 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tc'8 [ ]\n\tr4\n\tcs'8 [\n\td'8\n\tef'8 ]\n}"


def test_containertools_insert_component_and_fracture_crossing_spanners_03( ):
   '''Insert works just after a spanner.'''

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, 4, Rest((1, 4)))

   r'''
   \new Staff {
           c'8 [
           cs'8
           d'8
           ef'8 ]
           r4
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tc'8 [\n\tcs'8\n\td'8\n\tef'8 ]\n\tr4\n}"


def test_containertools_insert_component_and_fracture_crossing_spanners_04( ):
   '''Insert works with really big positive values.'''

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, 1000, Rest((1, 4)))

   r'''
   \new Staff {
           c'8 [
           cs'8
           d'8
           ef'8 ]
        r4
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tc'8 [\n\tcs'8\n\td'8\n\tef'8 ]\n\tr4\n}"


def test_containertools_insert_component_and_fracture_crossing_spanners_05( ):
   '''Insert works with negative values.'''

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, -1, Rest((1, 4)))

   r'''
   \new Staff {
           c'8 [
           cs'8
           d'8 ]
           r4
           ef'8 [ ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tc'8 [\n\tcs'8\n\td'8 ]\n\tr4\n\tef'8 [ ]\n}"


def test_containertools_insert_component_and_fracture_crossing_spanners_06( ):
   '''Insert works with really big negative values.'''

   t = Staff([Note(n, (1, 8)) for n in range(4)])
   Beam(t[:])
   containertools.insert_component_and_fracture_crossing_spanners(t, -1000, Rest((1, 4)))

   r'''
   \new Staff {
           r4
           c'8 [
           cs'8
           d'8
           ef'8 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\tr4\n\tc'8 [\n\tcs'8\n\td'8\n\tef'8 ]\n}"


def test_containertools_insert_component_and_fracture_crossing_spanners_07( ):
   '''Inserting a note from one container into another container
      switches note parent from first container to second.'''

   v = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(4))
   t = Staff(leaftools.make_repeated_notes(8))
   note = v[0]
   containertools.insert_component_and_fracture_crossing_spanners(t, 1, v[0])

   assert check.wf(v)
   assert check.wf(t)
   assert not note in v
   assert note.parentage.parent is t
