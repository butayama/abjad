from abjad.cfg.abjad_version import abjad_version
import time


def _write_abjad_header(outfile):
   cur_time = time.strftime('%Y-%m-%d %H:%M')
   outfile.write('%% Abjad revision %s\n' % abjad_version)
   outfile.write('%% %s\n\n' % cur_time)
