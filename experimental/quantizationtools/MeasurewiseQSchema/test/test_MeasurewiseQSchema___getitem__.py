from abjad.tools import contexttools
from experimental import quantizationtools


def test_MeasurewiseQSchema___getitem___01():

    schema = quantizationtools.MeasurewiseQSchema()

    assert schema[0] == schema[1] == schema[2] == {
        'search_tree': quantizationtools.OldSearchTree(),
        'tempo': contexttools.TempoMark((1, 4), 60),
        'time_signature': contexttools.TimeSignatureMark((4, 4)),
        'use_full_measure': False,
    }


def test_MeasurewiseQSchema___getitem___02():

    item_a = quantizationtools.MeasurewiseQSchemaItem(search_tree=quantizationtools.OldSearchTree({2: None}))
    item_b = quantizationtools.MeasurewiseQSchemaItem(tempo=((1, 4), 76))
    item_c = quantizationtools.MeasurewiseQSchemaItem(time_signature=(3, 4))
    item_d = quantizationtools.MeasurewiseQSchemaItem(
        search_tree={5: None},
        use_full_measure=True
        )

    schema = quantizationtools.MeasurewiseQSchema(
        {2: item_a, 4: item_b, 7: item_c, 8: item_d},
        search_tree=quantizationtools.OldSearchTree({3: None}),
        tempo=((1, 8), 58),
        time_signature=(5, 8),
        use_full_measure=False,
        )

    assert schema[0] == schema[1] == {
        'search_tree': quantizationtools.OldSearchTree({3: None}),
        'tempo': contexttools.TempoMark((1, 8), 58),
        'time_signature': contexttools.TimeSignatureMark((5, 8)),
        'use_full_measure': False,
    }

    assert schema[2] == schema[3] == {
        'search_tree': quantizationtools.OldSearchTree({2: None}),
        'tempo': contexttools.TempoMark((1, 8), 58),
        'time_signature': contexttools.TimeSignatureMark((5, 8)),
        'use_full_measure': False,
    }

    assert schema[4] == schema[5] == schema[6] == {
        'search_tree': quantizationtools.OldSearchTree({2: None}),
        'tempo': contexttools.TempoMark((1, 4), 76),
        'time_signature': contexttools.TimeSignatureMark((5, 8)),
        'use_full_measure': False,
    }

    assert schema[7] == {
        'search_tree': quantizationtools.OldSearchTree({2: None}),
        'tempo': contexttools.TempoMark((1, 4), 76),
        'time_signature': contexttools.TimeSignatureMark((3, 4)),
        'use_full_measure': False,
    }

    assert schema[8] == schema[9] == schema[1000] == {
        'search_tree': quantizationtools.OldSearchTree({5: None}),
        'tempo': contexttools.TempoMark((1, 4), 76),
        'time_signature': contexttools.TimeSignatureMark((3, 4)),
        'use_full_measure': True,
    }
