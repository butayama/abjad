# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageManager_revert_01():

    wrangler = score_manager._material_package_wrangler
    manager = wrangler._find_up_to_date_manager(
        repository='git',
        system=True,
        )

    assert manager._test_revert()


def test_MaterialPackageManager_revert_02():

    wrangler = score_manager._material_package_wrangler
    manager = wrangler._find_up_to_date_manager(
        repository='svn',
        system=False,
        )

    if not manager:
        return

    assert manager._test_revert()