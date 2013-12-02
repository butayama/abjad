# -*- encoding: utf-8 -*-
import inspect
import pytest
import abjad
from abjad.tools import documentationtools


classes = documentationtools.list_all_abjad_classes()
@pytest.mark.parametrize('class_', classes)
def test_storage_format_01(class_):
    r'''All storage-formattable classes have evaluable storage format.
    '''

    if '_storage_format_specification' in dir(class_) and \
        not inspect.isabstract(class_):
        instance_one = class_()
        instance_two = eval(format(instance_one, 'storage'), abjad.__dict__)
        assert instance_one == instance_two
