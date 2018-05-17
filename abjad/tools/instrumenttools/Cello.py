from .Instrument import Instrument


class Cello(Instrument):
    r"""
    Cello.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
        >>> clef = abjad.Clef('bass')
        >>> abjad.attach(clef, staff[0])
        >>> cello = abjad.Cello()
        >>> abjad.attach(cello, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \set Staff.instrumentName = \markup { Cello }
                \set Staff.shortInstrumentName = \markup { Vc. }
                \clef "bass"
                c'4
                d'4
                e'4
                fs'4
            }

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_default_tuning',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        name='cello',
        short_name='vc.',
        markup=None,
        short_markup=None,
        allowable_clefs=('bass', 'tenor', 'treble'),
        context=None,
        default_tuning=('C2', 'G2', 'D3', 'A3'),
        middle_c_sounding_pitch=None,
        pitch_range='[C2, G5]',
        hide=None,
        ):
        import abjad
        Instrument.__init__(
            self,
            name=name,
            short_name=short_name,
            markup=markup,
            short_markup=short_markup,
            allowable_clefs=allowable_clefs,
            context=context,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            hide=hide,
            )
        self._is_primary_instrument = True
        self._default_tuning = abjad.Tuning(default_tuning)

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        """
        Gets cello's allowable clefs.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.allowable_clefs
            ('bass', 'tenor', 'treble')

        Returns clef list.
        """
        return Instrument.allowable_clefs.fget(self)

    @property
    def default_tuning(self):
        """
        Gets cello's default tuning.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.default_tuning
            Tuning(pitches=PitchSegment(['c,', 'g,', 'd', 'a']))

        Returns tuning.
        """
        return self._default_tuning

    @property
    def markup(self):
        """
        Gets cello's instrument name markup.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.markup
            Markup(contents=['Cello'])

            >>> abjad.show(cello.markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        """
        Gets sounding pitch of cello's written middle C.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.middle_c_sounding_pitch
            NamedPitch("c'")

            >>> abjad.show(cello.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        """
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        """
        Gets cello's name.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.name
            'cello'

        Returns string.
        """
        return Instrument.name.fget(self)

    @property
    def pitch_range(self):
        """
        Gets cello's range.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.pitch_range
            PitchRange('[C2, G5]')

            >>> abjad.show(cello.pitch_range) # doctest: +SKIP

        Returns pitch range.
        """
        return Instrument.pitch_range.fget(self)

    @property
    def short_markup(self):
        """
        Gets cello's short instrument name markup.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.short_markup
            Markup(contents=['Vc.'])

            >>> abjad.show(cello.short_markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.short_markup.fget(self)

    @property
    def short_name(self):
        """
        Gets cello's short instrument name.

        ..  container:: example

            >>> cello = abjad.Cello()
            >>> cello.short_name
            'vc.'

        Returns string.
        """
        return Instrument.short_name.fget(self)
