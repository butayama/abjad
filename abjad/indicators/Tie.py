import typing

from abjad import enums
from abjad.lilypondnames.LilyPondTweakManager import LilyPondTweakManager
from abjad.system.LilyPondFormatBundle import LilyPondFormatBundle
from abjad.system.Tags import Tags
from abjad.top.inspect import inspect
from abjad.utilities.String import String

from ..format import StorageFormatManager

abjad_tags = Tags()


class Tie(object):
    r"""
    LilyPond ``~`` command.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 c' d' d'")
        >>> tie = abjad.Tie()
        >>> abjad.tweak(tie).color = 'blue'
        >>> abjad.attach(tie, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                c'4
                - \tweak color #blue
                ~
                c'4
                d'4
                d'4
            }

        >>> for leaf in staff:
        ...     leaf, abjad.inspect(leaf).logical_tie()
        ...
        (Note("c'4"), LogicalTie([Note("c'4"), Note("c'4")]))
        (Note("c'4"), LogicalTie([Note("c'4"), Note("c'4")]))
        (Note("d'4"), LogicalTie([Note("d'4")]))
        (Note("d'4"), LogicalTie([Note("d'4")]))

    """

    ### CLASS VARIABLES ###

    __slots__ = ("_direction", "_tweaks")

    _context = "Voice"

    _persistent = True

    _publish_storage_format = True

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        direction: enums.VerticalAlignment = None,
        tweaks: LilyPondTweakManager = None,
    ) -> None:
        direction_ = String.to_tridirectional_lilypond_symbol(direction)
        self._direction = direction_
        if tweaks is not None:
            assert isinstance(tweaks, LilyPondTweakManager), repr(tweaks)
        self._tweaks = LilyPondTweakManager.set_tweaks(self, tweaks)

    ### SPECIAL METHODS ###

    def __eq__(self, argument) -> bool:
        """
        Is true when all initialization values of Abjad value object equal
        the initialization values of ``argument``.
        """
        return StorageFormatManager.compare_objects(self, argument)

    def __hash__(self) -> int:
        """
        Hashes Abjad value object.
        """
        hash_values = StorageFormatManager(self).get_hash_values()
        try:
            result = hash(hash_values)
        except TypeError:
            raise TypeError(f"unhashable type: {self}")
        return result

    def __repr__(self) -> str:
        """
        Gets interpreter representation.
        """
        return StorageFormatManager(self).get_repr_format()

    ### PRIVATE METHODS ###

    def _add_direction(self, string):
        if getattr(self, "direction", None) is not None:
            string = f"{self.direction} {string}"
        return string

    def _attachment_test_all(self, argument):
        from abjad.core.Chord import Chord
        from abjad.core.Note import Note

        if not isinstance(argument, (Chord, Note)):
            string = f"Must be note or chord (not {argument})."
            return [string]
        next_leaf = inspect(argument).leaf(1)
        if not isinstance(next_leaf, (Chord, Note, type(None))):
            string = f"Can not attach tie to {argument}"
            string += f" when next leaf is {next_leaf}."
            return [string]
        return True

    def _get_lilypond_format_bundle(self, component=None):
        bundle = LilyPondFormatBundle()
        if self.tweaks:
            strings = self.tweaks._list_format_contributions()
            bundle.after.spanner_starts.extend(strings)
        string = self._add_direction("~")
        strings = [string]
        bundle.after.spanner_starts.extend(strings)
        return bundle

    ### PUBLIC PROPERTIES ###

    @property
    def context(self) -> str:
        """
        Returns (historically conventional) context ``'Voice'``.

        ..  container:: example

            >>> abjad.Tie().context
            'Voice'

        Class constant.

        Override with ``abjad.attach(..., context='...')``.
        """
        return self._context

    @property
    def direction(self) -> typing.Optional[str]:
        r"""
        Gets direction.

        ..  container:: example

            With ``direction`` unset:

            >>> staff = abjad.Staff("c'4 c' c'' c''")
            >>> abjad.attach(abjad.Tie(), staff[0])
            >>> abjad.attach(abjad.Tie(), staff[2])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    ~
                    c'4
                    c''4
                    ~
                    c''4
                }

            With ``direction=abjad.Up``:

            >>> staff = abjad.Staff("c'4 c' c'' c''")
            >>> abjad.attach(abjad.Tie(direction=abjad.Up), staff[0])
            >>> abjad.attach(abjad.Tie(direction=abjad.Up), staff[2])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    ^ ~
                    c'4
                    c''4
                    ^ ~
                    c''4
                }

            With ``direction=abjad.Down``:

            >>> staff = abjad.Staff("c'4 c' c'' c''")
            >>> abjad.attach(abjad.Tie(direction=abjad.Down), staff[0])
            >>> abjad.attach(abjad.Tie(direction=abjad.Down), staff[2])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    _ ~
                    c'4
                    c''4
                    _ ~
                    c''4
                }

        """
        return self._direction

    @property
    def persistent(self) -> bool:
        """
        Is true.

        ..  container:: example

            >>> abjad.Tie().persistent
            True

        Class constant.
        """
        return self._persistent

    @property
    def tweaks(self) -> typing.Optional[LilyPondTweakManager]:
        r"""
        Gets tweaks

        ..  container:: example

            >>> staff = abjad.Staff("c'4 c' d' d'")
            >>> tie = abjad.Tie()
            >>> abjad.tweak(tie).color = 'blue'
            >>> abjad.attach(tie, staff[0])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    - \tweak color #blue
                    ~
                    c'4
                    d'4
                    d'4
                }

        """
        return self._tweaks
