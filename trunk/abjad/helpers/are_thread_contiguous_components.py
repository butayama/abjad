from abjad.component.component import _Component
from abjad.helpers.iterate import iterate


def _are_thread_contiguous_components(expr):
   r'''True when expr is a Python list of Abjad components, and
      when there exists no foreign component C_f not in list such that
      C_f occurs temporally between any of the components in list.

      Thread-contiguous components are definitionally spannable.

      Example:

      t = Voice(run(4))
      t.insert(2, Voice(run(2)))
      Sequential(t[:2])
      Sequential(t[-2:])
      diatonicize(t)

      \new Voice {
         {
            c'8
            d'8
         }
         \new Voice {
            e'8
            f'8
         }
         {
            g'8
            a'8
         }
      }

      assert _are_thread_contiguous_components(t[0:1] + t[-1:])
      assert _are_thread_contiguous_components(t[0][:] + t[-1:])
      assert _are_thread_contiguous_components(t[0:1] + t[-1][:])
      assert _are_thread_contiguous_components(t[0][:] + t[-1][:])'''

   if not isinstance(expr, list):
      return False
   if len(expr) == 0:
      return True 
   first = expr[0]
   if not isinstance(first, _Component):
      return False
   first_thread = first.parentage._threadSignature
   prev = first
   for cur in expr[1:]:
      print prev, cur
      if not isinstance(cur, _Component):
         return False
      if not cur.parentage._threadSignature == first_thread:
         return False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         if not _are_thread_proper(prev, cur):
            return False
      prev = cur
   return True


def _are_thread_proper(component_1, component_2):
   '''True when

         1. component_1 and component_2 are both Abjad components,
         2. component_1 and component_2 share the same thread,
         3. component_1 precedes component_2 in temporal order, and
         4. there exists no intervening component x that both shares
            the same thread as component_1 and component_2 and
            that intervenes temporally between component_1 and _2.

      Otherwise False.'''

   ## if either input parameter are not Abjad tokens
   if not isinstance(component_1, _Component) or \
      not isinstance(component_2, _Component):
      #print 'not components!'
      return False

   ## if component_1 and component_2 do not share a thread
   first_thread = component_1.parentage._threadSignature
   if not first_thread == component_2.parentage._threadSignature:
      #print 'not same thread!'
      return False

   ## find component_1 offset end time and component_2 offset begin
   first_end = component_1.offset.score + component_1.duration.prolated
   second_begin = component_2.offset.score

   ## if component_1 does not preced component_2
   if not first_end <= second_begin:
      #print 'not temporally ordered!'
      return False

   ## if there exists an intervening component of the same thread
   dfs = component_1._navigator._DFS(capped = False)
   for node in dfs:
      if node is component_2:
         break
      node_thread = node.parentage._threadSignature
      if node_thread == first_thread:
         node_begin = node.offset.score
         if first_end <= node_begin < second_begin:
            print 'Component %s intervenes between %s and %s.' % \
               (node, component_1, component_2)
            return False

   ## otherwise, return True
   return True
