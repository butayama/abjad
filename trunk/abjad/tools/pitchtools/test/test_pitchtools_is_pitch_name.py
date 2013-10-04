# -*- encoding: utf-8 -*-
from abjad import *


def test_pitchtools_is_pitch_name_01():

    assert pitchtools.is_pitch_name('c,')
    assert pitchtools.is_pitch_name('cs,')
    assert pitchtools.is_pitch_name('c')
    assert pitchtools.is_pitch_name('cs')
    assert pitchtools.is_pitch_name("ctqs''")


def test_pitchtools_is_pitch_name_02():

    assert not pitchtools.is_pitch_name('foo')
    assert not pitchtools.is_pitch_name('c4')
