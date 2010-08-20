from abjad.core import _Abjad
from abjad.exceptions import ExtraSpannerError
from abjad.exceptions import MissingSpannerError


class _SpannerReceptor(_Abjad):
   '''Abstract base class to mix in with component interfaces.
   '''

   def __init__(self, klasses):
      '''`klasses` should be a tuple of one or more spanner classes.'''
      self._klasses = klasses

   ## PUBLIC ATTRIBUTES ##

   @property
   def chain(self):
      '''Return tuple of all leaves in spanner, if spanned;
         otherwise return 1-tuple of client.'''
      count = self.count
      if count == 0:
         return (self._client, )
      elif count == 1:
         return tuple(self.spanner.leaves)
      else:
         raise ExtraSpannerError

   @property
   def count(self):
      '''Return number of spanners attaching to client.'''
      #return len(self.spanners)
      from abjad.tools import spannertools
      return len(spannertools.get_all_spanners_attached_to_component(self._client, self._klasses))

   @property
   def first(self):
      '''True when client is first in spanner, otherwise False.'''
      #return self.spanned and self.spanner._is_my_first_leaf(self._client)
      from abjad.tools import spannertools
      if bool(spannertools.get_all_spanners_attached_to_component(self._client, self._klasses)):
         spanner = spannertools.get_the_only_spanner_attached_to_component(
            self._client, self._klasses)
         return spanner._is_my_first_leaf(self._client)

   @property
   def last(self):
      '''True when client is last in spanner, otherwise False.'''
      #return self.spanned and self.spanner._is_my_last_leaf(self._client)
      from abjad.tools import spannertools
      if bool(spannertools.get_all_spanners_attached_to_component(self._client, self._klasses)):
         spanner = spannertools.get_the_only_spanner_attached_to_component(
            self._client, self._klasses)
         return spanner._is_my_last_leaf(self._client)

   @property
   def only(self):
      '''True when client is only leaf in spanner, otherwise False.'''
      #return self.spanned and self.spanner._is_my_only_leaf(self._client)
      from abjad.tools import spannertools
      if bool(spannertools.get_all_spanners_attached_to_component(self._client, self._klasses)):
         spanner = spannertools.get_the_only_spanner_attached_to_component(
            self._client, self._klasses)
         return spanner._is_my_only_leaf(self._client)

   @property
   def parented(self):
      '''True when spanner attached to any component in parentage of client,
      including client, otherwise False.
      '''
#      result =  [ ]
#      parentage = self._client.parentage.parentage
#      for parent in parentage:
#         spanners = parent.spanners.attached
#         for klass in self._klasses:
#            result.extend(
#               [p for p in spanners if isinstance(p, klass)])
#      return bool(result)
      from abjad.tools import spannertools
      return bool(
         spannertools.get_all_spanners_attached_to_any_improper_parent_of_component(
            self._client, self._klasses))
      
   @property
   def position(self):
      '''Return zero-indexed position of client in spanner.'''
#      count = self.count
#      if count == 0:
#         raise MissingSpannerError
#      elif count == 1:
#         return self.spanner.index(self._client)
#      else:
#         raise ExtraSpannerError
      from abjad.tools import spannertools
      spanner = spannertools.get_the_only_spanner_attached_to_component(self._client, self._klasses)
      return spanner.index(self._client)

   @property
   def spanned(self):
      '''True when client is spanned.'''
      #return bool(self.spanners)
      from abjad.tools import spannertools
      return bool(spannertools.get_all_spanners_attached_to_component(self._client, self._klasses))


   @property
   def spanner(self):
      '''Return first spanner attaching to client.'''
#      count = self.count
#      if count == 0:
#         raise MissingSpannerError
#      elif count == 1:
#         return list(self.spanners)[0]
#      else:
#         raise ExtraSpannerError
      from abjad.tools import spannertools
      return spannertools.get_the_only_spanner_attached_to_component(self._client, self._klasses)

   @property
   def spanner_in_parentage(self):
      '''Return first spanner attaching to parentage of client.
      '''
#      parentage = self._client.parentage.parentage
#      for parent in parentage:
#         spanners = parent.spanners.attached
#         for klass in self._klasses:
#            for spanner in spanners:
#               if isinstance(spanner, klass):
#                  return spanner
#      raise MissingSpannerError
      from abjad.tools import spannertools
      return spannertools.get_the_only_spanner_attached_to_any_improper_parent_of_component(
         self._client, self._klasses)
      
   ## externalized as spannertools.get_all_spanners_attached_to_component(self._client, klass)
   @property
   def spanners(self):
      '''Return all spanners attaching to client.'''
#      result = set([ ])
#      client = self._client
#      for klass in self._klasses:
#         spanners = client.spanners.attached
#         result.update([p for p in spanners if isinstance(p, klass)])
#      return result
      from abjad.tools import spannertools
      return spannertools.get_all_spanners_attached_to_component(self._client, self._klasses)

   @property
   def spanners_attached_to_contents(self):
      '''Unordered set of all spanners attaching to
      any component in the contents of client, including client.'''
      from abjad.tools import spannertools
#      contained = set([ ])
#      for spanner in spannertools.get_spanners_contained_by_components([self._client]):
#         for klass in self._klasses:
#            if isinstance(spanner, klass):
#               contained.add(spanner)
#      return contained
      return spannertools.get_all_spanners_attached_to_any_improper_child_of_component(
         self._client, self._klasses)

   @property
   def spanners_in_parentage(self):
      '''.. versionadded:: 1.1.2

      Return unordered set of all spanners attaching to 
      any component in the parentage of client, including client.
      '''
#      result = set([ ])
#      parentage = self._client.parentage.parentage
#      for parent in parentage:
#         spanners = parent.spanners.attached
#         for klass in self._klasses:
#            for spanner in spanners:
#               if isinstance(spanner, klass):
#                  result.add(spanner)
#      return result
      from abjad.tools import spannertools
      return spannertools.get_all_spanners_attached_to_any_improper_parent_of_component(
         self._client, self._klasses)

   ## PUBLIC METHODS ##

   def unspan(self):
      '''Remove all spanners attaching to client.'''
#      result = [ ]
#      for spanner in list(self.spanners):
#         spanner.clear( )
#         result.append(spanner)
#      return result
      from abjad.tools import spannertools
      return spannertools.destroy_all_spanners_attached_to_component(self._client, self._klasses)
