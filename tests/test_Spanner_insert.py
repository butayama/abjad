import abjad


def test_Spanner_insert_01():
    """
    Insert component in spanner at index i.
    Add spanner to component's aggregator.
    Component then knows about spanner and vice versa.
    Not composer-safe.
    Inserting into middle of spanner may leave discontiguous spanner.
    """

    voice = abjad.Voice("c'8 d'8 e'8 f'8")
    slur = abjad.Slur()
    abjad.attach(slur, voice[:2])

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            c'8
            (
            d'8
            )
            e'8
            f'8
        }
        """
        )

    slur._insert(1, voice[:][-1])

    assert not abjad.inspect(voice).wellformed()


def test_Spanner_insert_02():
    """
    Insert component at index zero in spanner.
    This operation does not mangle spanner.
    Operation is still not composer-safe, however.
    """

    voice = abjad.Voice("{ c'8 d'8 } { e'8 f'8 } { g'8 a'8 }")
    beam = abjad.Beam()
    abjad.attach(beam, voice[1][:])

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                d'8
            }
            {
                e'8
                [
                f'8
                ]
            }
            {
                g'8
                a'8
            }
        }
        """
        )

    beam._insert(0, voice[0][1])

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                d'8
                [
            }
            {
                e'8
                f'8
                ]
            }
            {
                g'8
                a'8
            }
        }
        """
        )
