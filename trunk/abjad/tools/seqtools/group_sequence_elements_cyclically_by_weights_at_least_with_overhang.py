from abjad.tools.seqtools._group_sequence_elements_by_weights_at_least import \
   _group_sequence_elements_by_weights_at_least


def group_sequence_elements_cyclically_by_weights_at_least_with_overhang(sequence, weights):
   '''Group `sequence` elements cyclically by `weights` at least with overhang::

      abjad> sequence = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
      abjad> groups = seqtools.group_sequence_elements_cyclically_by_weights_at_least_with_overhang(sequence, [10, 4])
      [[3, 3, 3, 3], [4], [4, 4, 4], [5], [5]]

   Return list sequence element reference lists.
   '''

   return _group_sequence_elements_by_weights_at_least(
      sequence, weights, cyclic = True, overhang = True)
