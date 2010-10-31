from abjad.tools.seqtools._group_sequence_elements_by_weights_at_most import \
   _group_sequence_elements_by_weights_at_most


def group_sequence_elements_once_by_weights_at_most_without_overhang(sequence, weights):
   '''Group `sequence` elements once by `weights` at most without overhang::

      abjad> sequence = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
      abjad> groups = seqtools.group_sequence_elements_once_by_weights_at_most_without_overhang(sequence, [10, 4])
      [[3, 3, 3], [3]]

   Return list sequence element reference lists.
   '''

   return _group_sequence_elements_by_weights_at_most(
      sequence, weights, cyclic = False, overhang = False)
