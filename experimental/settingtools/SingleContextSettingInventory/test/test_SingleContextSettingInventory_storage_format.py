from abjad.tools import *
from experimental import *
from experimental.settingtools import SingleContextSettingInventory


def test_SingleContextSettingInventory_storage_format_01():
    '''Disk format exists and is evaluable.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)

    segment = score_specification.append_segment('red')
    segment.set_time_signatures([(4, 8), (3, 8)])
    score_specification.interpret()

    setting_inventory_1 = segment.single_context_settings

    storage_format = setting_inventory_1.storage_format

    r'''
    settingtools.SingleContextSettingInventory([
        settingtools.SingleContextSetting(
            'time_signatures',
            [(4, 8), (3, 8)],
            selectortools.TimespanSelector(
                timespantools.SingleSourceTimespan(
                    selector=selectortools.SegmentItemSelector(
                        identifier='red'
                        )
                    )
                ),
            context_name='Grouped Rhythmic Staves Score',
            persist=True,
            truncate=False,
            fresh=True
            )
        ])
    '''

    setting_inventory_2 = eval(storage_format)

    assert isinstance(setting_inventory_1, SingleContextSettingInventory)
    assert isinstance(setting_inventory_2, SingleContextSettingInventory)
    assert not setting_inventory_1 is setting_inventory_2
    assert setting_inventory_1 == setting_inventory_2
