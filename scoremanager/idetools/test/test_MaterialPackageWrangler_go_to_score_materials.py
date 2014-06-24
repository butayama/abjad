# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_go_to_score_materials_01():
    r'''From score materials to score materials.
    '''

    input_ = 'red~example~score m m q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - materials',
        ]
    assert score_manager._transcript.titles == titles