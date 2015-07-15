# -*- encoding: utf-8 -*-
import inspect
import pytest
from abjad.tools import datastructuretools
from abjad.tools import documentationtools


ignored_classes = (
    datastructuretools.Enumeration,
    )

classes = documentationtools.list_all_abjad_classes(
    ignored_classes=ignored_classes,
    )


@pytest.mark.parametrize('class_', classes)
def test_abjad___hash___01(class_):
    r'''All concrete classes with __hash__ can hash.
    '''
    if inspect.isabstract(class_):
        return
    if getattr(class_, '__hash__', None) is None:
        return
    instance = class_()
    value = hash(instance)
    assert isinstance(value, int)