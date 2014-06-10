# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageManager_unset_autoeditor_01():

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'materials',
        'test_tempo_inventory',
        )

    with systemtools.FilesystemState(remove=[path]):
        input_ = 'red~example~score m new test~tempo~inventory y'
        input_ += ' aes TempoInventory <return> q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents
        string = 'test tempo inventory (AE)'
        assert string in contents
        input_ = 'red~example~Score m test~tempo~inventory aeu q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents
        string = 'test tempo inventory\n'
        assert string in contents