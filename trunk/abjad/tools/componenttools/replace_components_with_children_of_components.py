from abjad.tools import check
from abjad.tools import parenttools


def replace_components_with_children_of_components(components):
   r'''Remove arbitrary `components` from score 
   but retain children of `components` in score. ::

      abjad> staff = Staff(Container(leaftools.make_repeated_notes(2)) * 2)
      abjad> pitchtools.diatonicize(staff)
      abjad> Slur(staff[:])
      abjad> Beam(staff.leaves)
      abjad> f(staff)
      \new Staff {
         {
            c'8 [ (
            d'8
         }
         {
            e'8
            f'8 ] )
         }
      }
      
   ::
      
      abjad> componenttools.replace_components_with_children_of_components(staff[0:1])
      [{ }]
      
   ::
      
      abjad> f(staff)
      \new Staff {
         c'8 [ (
         d'8
         {
            e'8
            f'8 ] )
         }
      }

   Return `components`.

   .. note:: should be renamed to 
      ``componenttools.remove_components_from_score_shallow( )``

   .. versionchanged:: 1.1.2
      renamed ``componenttools.slip( )`` to
      ``componenttools.replace_components_with_children_of_components( )``.
   '''

   check.assert_components(components)
   for component in components:
      parent, start, stop = parenttools.get_with_indices([component])
      result = parent[start:stop+1] = list(component.music)
   return components
