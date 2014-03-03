# -*- encoding: utf-8 -*-
from abjad import *
from scoremanager.managers.MaterialManager import MaterialManager


class OctaveTranspositionMappingInventoryMaterialManager(MaterialManager):

    ### INITIALIZER ###

    def __init__(self, filesystem_path=None, session=None):
        superclass = super(
            OctaveTranspositionMappingInventoryMaterialManager, 
            self,
            )
        superclass.__init__(filesystem_path=filesystem_path, session=session)
        self._generic_output_name = 'octave transposition mapping inventory'
        self._output_material_module_import_statements = [
            'from abjad import *',
            ]

    ### SPECIAL METHODS ###

    @staticmethod
    def __illustrate__(octave_transposition_mapping_inventory, **kwargs):
        notes = []
        for mapping in octave_transposition_mapping_inventory:
            note = Note("c'4")
            notes.append(note)
        staff = scoretools.Staff(notes)
        staff.context_name = 'RhythmicStaff'
        score = Score([staff])
        illustration = lilypondfiletools.make_basic_lilypond_file(score)
        vector = layouttools.make_spacing_vector(0, 0, 6, 0)
        illustration.paper_block.top_system_spacing = vector
        override(score).note_head.transparent = True
        override(score).bar_line.transparent = True
        override(score).clef.transparent = True
        override(score).span_bar.transparent = True
        override(score).staff_symbol.transparent = True
        override(score).stem.transparent = True
        override(score).time_signature.stencil = False
        moment = schemetools.SchemeMoment(1, 24)
        set_(score).proportional_notation_duration = moment
        return illustration

    ### PUBLIC METHODS ###
        
    @staticmethod
    def _check_output_material(material):
        return isinstance(
            material, 
            pitchtools.OctaveTranspositionMappingInventory,
            )

    @staticmethod
    def _get_output_material_editor(target=None, session=None):
        from scoremanager import editors
        editor = editors.OctaveTranspositionMappingInventoryEditor(
            session=session,
            target=target,
            )
        return editor

    @staticmethod
    def _make_output_material():
        return pitchtools.OctaveTranspositionMappingInventory