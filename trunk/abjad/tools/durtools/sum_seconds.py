def sum_seconds(components):
   r'''Sum the duration of `components` in seconds.

   ::

      abjad> tuplet = FixedDurationTuplet((2, 8), construct.scale(3))
      abjad> tempo_spanner = TempoSpanner([tuplet])
      abjad> tempo_indication = tempotools.TempoIndication(Rational(1, 4), 48)
      abjad> tempo_spanner.tempo_indication = tempo_indication
      abjad> f(tuplet)
      \times 2/3 {
         \tempo 4=48
         c'8
         d'8
         e'8
         %% tempo 4=48 ends here
      }
      abjad> durtools.sum_seconds(tuplet[:])
      Rational(5, 4)
   '''

   assert isinstance(components, list)
   return sum([component.duration.seconds for component in components])
