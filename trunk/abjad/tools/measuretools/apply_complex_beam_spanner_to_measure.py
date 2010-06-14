from abjad.measure import _Measure
from abjad.spanners import BeamComplexDurated


def apply_complex_beam_spanner_to_measure(measure):
   r'''.. versionadded:: 1.1.2

   Apply complex beam spanner to `measure`::

      abjad> measure = RigidMeasure((2, 8), leaftools.make_first_n_notes_in_ascending_diatonic_scale(2))
      abjad> f(measure)
      {
         \time 2/8
         c'8
         d'8
      }
      
   ::
      
      abjad> measuretools.apply_complex_beam_spanner_to_measure(measure)
      BeamComplexDurated(|2/8(2)|)
      
   ::
      
      abjad> f(measure)
      {
         \time 2/8
         \set stemLeftBeamCount = #0
         \set stemRightBeamCount = #1
         c'8 [
         \set stemLeftBeamCount = #1
         \set stemRightBeamCount = #0
         d'8 ]
      }


   Return complex beam spanner.
   '''
   
   ## check measure type
   if not isinstance(measure, _Measure):
      raise TypeError('must be measure: %s' % measure)

   ## apply complex beam spanner to measure
   beam = BeamComplexDurated(measure)

   ## return beam spanner
   return beam
