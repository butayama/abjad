from abjad.spanners import Beam
from abjad.spanners import BeamComplexDurated
from abjad.tools import iterate


def beam(expr, style = 'complex'):
   '''Expr can be any Abjad expression.
   Style must be 'complex' or None.

   Iterate expr. For every measure in expr,
   apply BeamComplexDurated, Beam for style set
   equal to 'complex', None, respectively.

   Return list of measures treated.
   '''

   measures_treated = [ ]
   for measure in iterate.measures_forward_in(expr):
      if style == 'complex':
         BeamComplexDurated(measure)
      elif style is None:
         Beam(measure)
      else:
         raise ValueError('unknown beam style.')
      measures_treated.append(measure)

   return measures_treated
