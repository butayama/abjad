# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_UserInputGetter_go_to_all_scores_01():

    score_manager = scoremanager.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score m tempo~inventory da 1 d S q'
    score_manager._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - materials - tempo inventory',
        'Red Example Score (2013) - materials - tempo inventory (EDIT)',
        'Red Example Score (2013) - materials - tempo inventory - tempo (EDIT)',
        'Abjad IDE - scores',
        ]
    assert score_manager._transcript.titles == titles