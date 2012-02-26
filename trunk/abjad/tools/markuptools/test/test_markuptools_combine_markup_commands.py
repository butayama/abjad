from abjad.tools.markuptools import MarkupCommand
from abjad.tools.markuptools import combine_markup_commands
from abjad.tools.schemetools import SchemePair


def test_markuptools_combine_markup_commands_01():

    markup_a = MarkupCommand('draw-circle', 4, 0.4, False)
    markup_b = MarkupCommand('filled-box', SchemePair(-4, 4), SchemePair(-0.5, 0.5), 1)
    markup_c = "some text"
    assert combine_markup_commands(markup_a, markup_b, markup_c).format == \
        "\\combine \\combine \\draw-circle #4 #0.4 ##f \\filled-box #'(-4 . 4) #'(-0.5 . 0.5) #1 #\"some text\""


def test_markuptools_combine_markup_commands_02():

    markup_a = 'only a little text'
    assert combine_markup_commands(markup_a) == markup_a
