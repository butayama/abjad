from abjad.component import _Component
from abjad.tools import iterate
import types


## TODO: Make check.assess_components( ) work with generators 
##       This will prevent needing to manifest large lists
##       of leaves for checking wiht check.assess_components( ).

def assess_components(expr, klasses = (_Component, ), 
   contiguity = None, share = None, allow_orphans = True):
   r'''Test `expr`. Return true or false depending on the
   combination of values of the four keyword parameters.
   Set `contiguity` to ``'strict'``, ``'thread'`` or ``None``.
   Set `share` to ``'parent'``, ``'score'``, ``'thread'`` or ``None``.
   The word 'assess' in the name of this function is meant to
   contrast with 'assert' in other functions defined in this package.
   This function returns true or false but raises no exceptions.
   Functions named with 'assert' raise exceptions instead of
   returning true or false.

   Examples all refer to the following score. ::

      abjad> first_voice = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(3))
      abjad> second_voice = Voice(leaftools.make_first_n_notes_in_ascending_diatonic_scale(2))
      abjad> pitchtools.diatonicize([first_voice, second_voice])
      abjad> staff = Staff([first_voice, second_voice])
      abjad> f(staff)
      \new Staff {
              \new Voice {
                      c'8
                      d'8
                      e'8
              }
              \new Voice {
                      f'8
                      g'8
              }
      }

   With ``contiguity == 'strict'`` and ``share == 'parent'``:

      True for strictly contiguous components that share the same parent::

         abjad> first_voice[1:]
         [Note(d', 8), Note(e', 8)]
         abjad> check.assess_components(first_voice[1:], contiguity = 'strict', share = 'parent')
         True

      False for noncontiguous components::

         abjad> (first_voice[0], first_voice[-1])
         (Note(c', 8), Note(e', 8))
         abjad> check.assess_components(first_voice[0], first_voice[-1]), contiguity = 'strict', share = 'parent')
         False

      False for components that do not share the same parent::

         abjad> staff.leaves   
         (Note(c', 8), Note(d', 8), Note(e', 8), Note(f', 8), Note(g', 8))
         abjad> check.assess_components(staff.leaves, contiguity = 'strict', share = 'parent')
         False

   With ``contiguity == 'strict'`` and ``share == 'score'``:

      True for strictly contiguous components that share the same score::

         abjad> staff.leaves
         (Note(c', 8), Note(d', 8), Note(e', 8), Note(f', 8), Note(g', 8))
         abjad> check.assess_components(staff.leaves, contiguity = 'strict', share = 'score')
         True

      False for noncontiguous components::

         abjad> (first_voice[0], first_voice[-1])
         (Note(c', 8), Note(e', 8))
         abjad> check.assess_components(first_voice[0], first_voice[-1]), contiguity = 'strict', share = 'parent')
         False

   The `allow_orphans` keyword works as a type of bypass.

   If `allow_orphans` is set to true 
   and if `expr` is a Python list of orphan components,
   then the function will always evaluate to true, regardless
   of the checks specified by the other keywords.

   On the other hand, if the `allow_orphans` keyword is set
   to false, then `expr` must meet the checks specified by the
   other keywords in order for the function to evaluate to true.

   Calls to this function appear at the beginning of many functions.  
   Calls to this function also iterate all elements in input.
   Initial performance testing indicates that this function is

   .. todo:: eliminate keywords and break this function into
      a family of nine related functions with longer names.
   '''

   if contiguity is None:
      
      if share is None:
         return __are_components(expr, klasses = klasses)

      elif share == 'parent':
         return __are_components_in_same_parent(expr, 
            klasses = klasses, allow_orphans = allow_orphans)

      elif share == 'score':
         return __are_components_in_same_score(expr, 
            klasses = klasses, allow_orphans = allow_orphans)

      elif share == 'thread':
         return __are_components_in_same_thread(expr, 
            klasses = klasses, allow_orphans = allow_orphans)

      else:
         raise ValueError(
            "share must be 'parent', 'score', 'thread' or None.")

   elif contiguity == 'strict':
   
      if share is None:
         return __are_strictly_contiguous_components(
            expr, klasses = klasses, allow_orphans = allow_orphans)

      elif share == 'parent':
         return __are_strictly_contiguous_components_in_same_parent(
            expr, klasses = klasses, allow_orphans = allow_orphans)

      elif share == 'score':
         return __are_strictly_contiguous_components_in_same_score(
            expr, klasses = klasses, allow_orphans = allow_orphans)

      elif share == 'thread':
         return __are_strictly_contiguous_components_in_same_thread(
            expr, klasses = klasses, allow_orphans = allow_orphans)

      else:
         raise ValueError(
            "share must be 'parent', 'score', 'thread' or None.")

   elif contiguity == 'thread':

      if share is not None:
         raise ValueError('When checking for thread-contiguity,'
            " the 'share' keyword should not be set.")

      else:
         return __are_thread_contiguous_components(
            expr, klasses = klasses, allow_orphans = allow_orphans)

   else:
      raise ValueError("'contiguity' must be 'strict', 'thread' or None.")


## MANGLED MODULE FUNCTIONS BELOW ##

def __are_components(expr, klasses = (_Component, )):
   '''True when expr is a Python list of Abjad components.
      otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('expr must be a list of Abjad components.')

   for element in expr:
      if not isinstance(element, klasses):
         return False

   return True



def __are_components_in_same_parent(expr, klasses = (_Component, ), 
   allow_orphans = True):
   '''True when expr is a Python list of Abjad components,
      and when all components have a parent and have the same parent.
      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True 

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   first_parent = first.parentage.parent
   if first_parent is None and not allow_orphans:
      return False

   for element in expr[1:]:
      if not isinstance(element, klasses):
         return False
      if element.parentage.parent is not first_parent:
         return False

   return True



def __are_components_in_same_score(expr, klasses = (_Component, ), 
   allow_orphans = True):
   '''True when expr is a Python list of Abjad components,
      and when all components have the same score root.
      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')
      
   if len(expr) == 0:
      return True 

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   first_parent = first.parentage.parent
   first_score = first.parentage.root
   for element in expr[1:]:
      if not isinstance(element, klasses):
         return False
      if element.parentage.root is not first_score:
         if not (allow_orphans and element.parentage.orphan):
            return False

   return True



def __are_components_in_same_thread(expr, klasses = (_Component, ), 
   allow_orphans = True):
   '''True when expr is a Python list of Abjad components such
      that all components in list carry the same thread signature.

      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   orphan_components = True
   if not first.parentage.orphan:
      orphan_components = False

   same_thread = True

   first_signature = first.thread.signature
   for component in expr[1:]:
      if not component.parentage.orphan:
         orphan_components = False
      if component.thread.signature != first_signature:
         same_thread = False
      if not allow_orphans and not same_thread:
         return False
      if allow_orphans and not orphan_components and not same_thread:
         return False

   return True



def __are_strictly_contiguous_components(expr, klasses = (_Component, ), 
   allow_orphans = True):
   '''True expr is a Python list of strictly contiguous components.
      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   orphan_components = True
   if not first.parentage.orphan:
      orphan_components = False

   strictly_contiguous = True

   prev = first
   for cur in expr[1:]:
      if not isinstance(cur, klasses):
         return False
      if not cur.parentage.orphan:
         orphan_components = False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         strictly_contiguous = False
      if (not allow_orphans or (allow_orphans and not orphan_components)) and \
         not strictly_contiguous:
         return False
      prev = cur

   return True



def __are_strictly_contiguous_components_in_same_parent(
   expr, klasses = (_Component, ), allow_orphans = True):
   '''True when expr is a Python list of Abjad components such that

         1. all components in list are strictly contiguous, and
         2. every component in list has the same parent.

      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   first_parent = first.parentage.parent
   if first_parent is None:
      if allow_orphans:
         orphan_components = True
      else:
         return False
   
   same_parent = True
   strictly_contiguous = True

   prev = first
   for cur in expr[1:]:
      if not isinstance(cur, klasses):
         return False
      if not cur.parentage.orphan:
         orphan_components = False
      if not cur.parentage.parent is first_parent:
         same_parent = False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         strictly_contiguous = False
      if (not allow_orphans or (allow_orphans and not orphan_components)) and \
         (not same_parent or not strictly_contiguous):
         return False
      prev = cur

   return True



def __are_strictly_contiguous_components_in_same_score(
   expr, klasses = (_Component), allow_orphans = True):
   '''True when expr is a Python list of Abjad components such that

         1. all components in list are strictly contiguous, and
         2. every component in list is in the same score.

      Otherwise False.'''

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   orphan_components = True   
   if not first.parentage.orphan:
      orphan_components = False

   same_score = True
   strictly_contiguous = True

   first_score = first.parentage.root
   prev = first
   for cur in expr[1:]:
      if not isinstance(cur, klasses):
         return False
      if not cur.parentage.orphan:
         orphan_components = False
      if not cur.parentage.root is first_score:
         same_score = False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         strictly_contiguous = False
      if (not allow_orphans or (allow_orphans and not orphan_components)) and \
         (not same_score or not strictly_contiguous):
         return False
      prev = cur

   return True


def __are_strictly_contiguous_components_in_same_thread(
   expr, klasses = (_Component), allow_orphans = True):
   '''True when expr is a Python list of Abjad components such that
         
         1. all components in list are strictly contiguous, and
         2. all components in list are in the same thread.

      Otherwise False.'''
   
   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   orphan_components = True
   if not first.parentage.orphan:
      orphan_components = False

   same_thread = True
   strictly_contiguous = True

   first_signature = first.thread.signature
   prev = first
   for cur in expr[1:]:
      if not isinstance(cur, klasses):
         return False
      if not cur.parentage.orphan:
         orphan_components = False
      cur_signature = cur.thread.signature
      if not cur_signature == first_signature:
         same_thread = False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         strictly_contiguous = False
      if (not allow_orphans or (allow_orphans and not orphan_components)) and \
         (not same_thread or not strictly_contiguous):
         return False
      prev = cur

   return True



def __are_thread_contiguous_components(expr, klasses = (_Component), 
   allow_orphans = True):
   r'''True when *expr* is a Python list of Abjad components, and
      when there exists no foreign component C_f not in list such that
      C_f occurs temporally between any of the components in list.

      Thread-contiguous components are definitionally spannable.

      Example::

         t = Voice(leaftools.make_repeated_notes(4))
         t.insert(2, Voice(leaftools.make_repeated_notes(2)))
         Container(t[:2])
         Container(t[-2:])
         pitchtools.diatonicize(t)

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

   if not isinstance(expr, (list, tuple, types.GeneratorType)):
      raise TypeError('Must be list of Abjad components.')

   if len(expr) == 0:
      return True 

   first = expr[0]
   if not isinstance(first, klasses):
      return False

   orphan_components = True
   if not first.parentage.orphan:
      orphan_components = False

   same_thread = True
   thread_proper = True

   first_thread = first.thread.signature
   prev = first
   for cur in expr[1:]:
      if not isinstance(cur, klasses):
         return False
      if not cur.parentage.orphan:
         orphan_components = False
      if not cur.thread.signature == first_thread:
         same_thread = False
      if not prev._navigator._isImmediateTemporalSuccessorOf(cur):
         if not _are_thread_proper(prev, cur):
            thread_proper = False
      if (not allow_orphans or (allow_orphans and not orphan_components)) and \
         (not same_thread or not thread_proper):
         return False
      prev = cur

   return True


def _are_thread_proper(component_1, component_2, klasses = (_Component)):
   '''True when

         1. component_1 and component_2 are both Abjad components,
         2. component_1 and component_2 share the same thread,
         3. component_1 precedes component_2 in temporal order, and
         4. there exists no intervening component x that both shares
            the same thread as component_1 and component_2 and
            that intervenes temporally between component_1 and _2.

      Otherwise False.'''

   ## if either input parameter are not Abjad tokens
   if not isinstance(component_1, klasses) or \
      not isinstance(component_2, klasses):
      return False

   ## if component_1 and component_2 do not share a thread
   first_thread = component_1.thread.signature
   if not first_thread == component_2.thread.signature:
      #print 'not same thread!'
      return False

   ## find component_1 offset end time and component_2 offset begin
   first_end = component_1.offset.prolated.stop
   second_begin = component_2.offset.prolated.start

   ## if component_1 does not preced component_2
   if not first_end <= second_begin:
      #print 'not temporally ordered!'
      return False

   ## if there exists an intervening component of the same thread
   dfs = component_1._navigator._DFS(capped = False)
   for node in dfs:
      if node is component_2:
         break
      node_thread = node.thread.signature
      if node_thread == first_thread:
         node_begin = node.offset.prolated.start
         if first_end <= node_begin < second_begin:
            print 'Component %s intervenes between %s and %s.' % \
               (node, component_1, component_2)
            return False

   ## otherwise, return True
   return True
