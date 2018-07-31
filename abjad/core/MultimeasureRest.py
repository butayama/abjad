import typing
from abjad.system.LilyPondFormatManager import LilyPondFormatManager
from .Leaf import Leaf
from .Rest import Rest


class MultimeasureRest(Leaf):
    """
    Multimeasure rest.

    ..  container:: example

        >>> rest = abjad.MultimeasureRest((1, 4))
        >>> abjad.show(rest) # doctest: +SKIP

    ..  container:: example

        >>> rest = abjad.MultimeasureRest('R1', tag='GLOBAL_MULTIMEASURE_REST')
        >>> abjad.f(rest)
        R1 %! GLOBAL_MULTIMEASURE_REST

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Leaves'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self, *arguments, tag: str = None) -> None:
        if len(arguments) == 0:
            arguments = ((1, 4),)
        rest = Rest(*arguments)
        Leaf.__init__(self, rest.written_duration, tag=tag)

    ### PRIVATE METHODS ###

    def _get_body(self):
        """
        Gets list of string representation of body of rest.
        Picked up as format contribution at format-time.
        """
        result = 'R' + str(self._get_formatted_duration())
        return [result]

    def _get_compact_representation(self):
        return f'R{self._get_formatted_duration()}'

    ### PUBLIC PROPERTIES ###

    @property
    def tag(self) -> typing.Optional[str]:
        r"""
        Gets tag.

        ..  container:: example

            >>> rest = abjad.MultimeasureRest(1, tag='MULTIMEASURE_REST')
            >>> multiplier = abjad.Multiplier(3, 8)
            >>> abjad.attach(multiplier, rest)

            >>> abjad.f(rest)
            R1 * 3/8 %! MULTIMEASURE_REST

        """
        return super().tag
