from abjad.component import _Component 
from abjad.spanners import Spanner


def iterate_components_forward(spanner, klass = _Component):
   '''.. versionadded:: 1.1.2

   Yield components in `spanner` one at a time from left to right. ::

      abjad> t = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(4))
      abjad> p = Beam(t[2:])
      abjad> notes = spannertools.iterate_components_forward(p, class = Note)
      abjad> for note in notes:
         print note
      Note(e', 8)
      Note(f', 8)
   '''

   if not isinstance(spanner, Spanner):
      raise TypeError

   for component in spanner._components:
      for node in component._navigator._DFS( ):
         if isinstance(node, klass):
            yield node
