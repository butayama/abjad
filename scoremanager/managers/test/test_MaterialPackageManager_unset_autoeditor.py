# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageManager_unset_autoeditor_01():

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'materials',
        'test_tempo_inventory',
        )

    with systemtools.FilesystemState(remove=[path]):
        input_ = 'red~example~score m new test~tempo~inventory'
        input_ += ' psa TempoInventory default q'
        score_manager._run(pending_input=input_)
        contents = score_manager._transcript.contents
        string = 'Package autoeditor set for TempoInventory.'
        assert string in contents
        input_ = 'red~example~Score m test~tempo~inventory pua q'
        score_manager._run(pending_input=input_)
        contents = score_manager._transcript.contents
        string = 'Package autoeditor set to none.'
        assert string in contents