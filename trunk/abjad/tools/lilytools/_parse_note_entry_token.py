from abjad.exceptions import InputSpecificationError
from abjad.note import Note
from abjad.pitch import Pitch
from abjad.rest import Rest
from abjad.skip import Skip
from abjad.tools import pitchtools
from abjad.tools.lilytools._lilypond_leaf_regex import _lilypond_leaf_regex
from abjad.tools.lilytools._parse_chord_entry_token import \
   _parse_chord_entry_token
import re


def _parse_note_entry_token(note_entry_token):
   '''.. versionadded:: 1.1.2

   Parse simple LilyPond `note_entry_token`. ::

      abjad> _parse_note_entry_token("c'4.")
      Note(c', 4.)

   ::

      abjad> _parse_note_entry_token('r8')  
      Rest(8)
   '''

   if not isinstance(note_entry_token, str):
      raise TypeError('LilyPond input token must be string.')

   pattern = _lilypond_leaf_regex
   match = re.match(pattern, note_entry_token)
   if match is None:
      ## TODO: make this work; change outer loop. ##
      #if note_entry_token.startswith('<'):
      #   chord = _parse_chord_entry_token(note_entry_token)
      #   return chord
      message = 'incorrect note entry token %s.' % note_entry_token
      raise InputSpecificationError(message)

   name, ticks, duration_body, dots = match.groups( )
   duration_string = duration_body + dots

   if name == 'r':
      return Rest(duration_string)
   elif name == 's':
      return Skip(duration_string)
   else:
      pitch_string = name + ticks
      pitch = Pitch(pitch_string)
      return Note(pitch, duration_string)
