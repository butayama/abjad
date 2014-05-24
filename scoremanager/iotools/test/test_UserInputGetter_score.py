# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_UserInputGetter_score_01():

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    input_ = 'red~example~score m tempo~inventory ae 1 d s q'
    score_manager._run(input_=input_)

    titles = [
        'Score Manager - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - materials - tempo inventory (AE)',
        'Red Example Score (2013) - materials - tempo inventory (AE) - tempo inventory',
        'Red Example Score (2013) - materials - tempo inventory (AE) - tempo inventory - tempo',
        'Red Example Score (2013)',
        ]
    assert score_manager._transcript.titles == titles