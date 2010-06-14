from abjad.tools import mathtools
from abjad.tools.containertools.rest_by_count import rest_by_count


def rest_half(container, rested_half, bigger_half, 
   rest_direction = 'automatic'):
   r'''Turn the left half of `container` into rests with the left
   half of `container` holding a greater number of elements
   than the right half::

      abjad> staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(9))
      abjad> containertools.rest_half(staff, 'left', 'left')
      abjad> f(staff)
      \new Staff {
         r8
         r2
         a'8
         b'8
         c''8
         d''8
      }
      
   Turn the left half of `container` into rests with the right
   half of `container` holding a greater number of elements
   than the left half::
      
      abjad> staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(9))
      abjad> containertools.rest_half(staff, 'left', 'right')
      abjad> f(staff)
      \new Staff {
         r2
         g'8
         a'8
         b'8
         c''8
         d''8
      }
      
   Turn the right half of `container` into rests with the left
   half of `container` holding a greater number of elements
   than the right half::
      
      abjad> staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(9))
      abjad> containertools.rest_half(staff, 'right', 'left')
      abjad> f(staff)
      \new Staff {
         c'8
         d'8
         e'8
         f'8
         g'8
         r2
      }
      
   Turn the right half of `container` into rests with the right
   half of `container` holding a greater number of elements
   than the left half::
      
      abjad> staff = Staff(leaftools.make_first_n_notes_in_ascending_diatonic_scale(9))
      abjad> containertools.rest_half(staff, 'right', 'right')
      abjad> f(staff)
      \new Staff {
         c'8
         d'8
         e'8
         f'8
         r2
         r8
      }
   
   
   Function works by the number of elements in `container`
   rather than by the duration of elements in `container`.

   Containers with an odd number of elements
   read `bigger_half` to decide whether 
   more elements on the left or right will group together.

   Containers with an even number of elements
   ignore `bigger_half`.

   Set `rest_direction` to ``'automatic'``, ``'big-endian'`` or 
   ``'little-endian'``.

   Return `container`.

   .. todo:: replace with a family of functions.
   '''

   ## assert input types
   assert rested_half in ('left', 'right')
   assert bigger_half in ('left', 'right')
   assert rest_direction in ('automatic', 'big-endian', 'little-endian')

   ## do nothing to empty containers or containers of length 1
   container_length = len(container)
   if container_length in (0, 1):
      return container

   ## determine split index
   halves = mathtools.partition_integer_into_halves(
      len(container), bigger = bigger_half)
   i = halves[0]

   ## rest container in place at split index
   rest_by_count(
      container, i, rested_half, direction = rest_direction)

   ## return rested container
   return container
