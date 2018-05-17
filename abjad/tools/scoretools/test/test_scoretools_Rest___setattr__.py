import abjad
import pytest


def test_scoretools_Rest___setattr___01():
    """
    Slots constrain rest attributes.
    """

    rest = abjad.Rest((1, 4))

    assert pytest.raises(AttributeError, "rest.foo = 'bar'")
