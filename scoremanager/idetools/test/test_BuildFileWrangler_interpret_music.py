# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_interpret_music_01():
    r'''Makes music.pdf when music.pdf doesn't yet exist.
    '''

    ly_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'music.ly',
        )
    pdf_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'music.pdf',
        )

    with systemtools.FilesystemState(keep=[ly_path, pdf_path]):
        os.remove(pdf_path)
        assert not os.path.exists(pdf_path)
        input_ = 'red~example~score u mi q'
        ide._run(input_=input_)
        assert os.path.isfile(pdf_path)
        assert systemtools.TestManager.compare_lys(
            ly_path,
            ly_path + '.backup',
            )
        assert systemtools.TestManager.compare_pdfs(
            pdf_path,
            pdf_path + '.backup',
            )


def test_BuildFileWrangler_interpret_music_02():
    r'''Preserves music.pdf when music.candidate.pdf compares
    equal to music.pdf.
    '''

    ly_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'music.ly',
        )
    pdf_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'music.pdf',
        )

    with systemtools.FilesystemState(keep=[ly_path, pdf_path]):
        input_ = 'red~example~score u mi q'
        ide._run(input_=input_)

    contents = ide._transcript.contents
    assert 'The files ...' in contents
    assert '... compare the same.' in contents
    assert 'Preserved' in contents