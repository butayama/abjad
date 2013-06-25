import os
import sys
from abjad.tools import stringtools
from experimental.tools.scoremanagertools.proxies.FileProxy import FileProxy


class ModuleProxy(FileProxy):

    ### INITIALIZER ###

    def __init__(self, packagesystem_path=None, session=None):
        assert packagesystem_path is None or os.path.sep not in packagesystem_path, repr(packagesystem_path)
        self._packagesystem_path = packagesystem_path
        filesystem_path = self.configuration.packagesystem_path_to_filesystem_path(
            self.packagesystem_path, is_module=True)
        FileProxy.__init__(self, filesystem_path=filesystem_path, session=session)

    ### CLASS VARIABLES ###

    extension = '.py'
    _generic_class_name = 'module'
    _temporary_asset_name = 'temporary_module.py'

    ### PRIVATE PROPERTIES ###

    @property
    def _space_delimited_lowercase_name(self):
        if self.filesystem_basename:
            name_without_extension = self.filesystem_basename.strip(self.extension)
            return stringtools.string_to_space_delimited_lowercase(name_without_extension)

    ### PRIVATE METHODS ###

    def _space_delimited_lowercase_name_to_asset_name(self, space_delimited_lowercase_name):
        asset_name = FileProxy._space_delimited_lowercase_name_to_asset_name(
            self, space_delimited_lowercase_name)
        asset_name += '.py'
        return asset_name

    ### PUBLIC PROPERTIES ###

    @property
    def packagesystem_basename(self):
        if self.packagesystem_path:
            return self.packagesystem_path.split('.')[-1]

    @property
    def packagesystem_path(self):
        return self._packagesystem_path

    @property
    def parent_directory_filesystem_path(self):
        if self.packagesystem_path:
            return self.configuration.packagesystem_path_to_filesystem_path(
                self.parent_directory_packagesystem_path)

    @property
    def parent_directory_packagesystem_path(self):
        if self.packagesystem_path:
            return '.'.join(self.packagesystem_path.split('.')[:-1])

    ### PUBLIC METHODS ###

    def execute_file_lines(self):
        if self.filesystem_path:
            file_pointer = open(self.filesystem_path, 'r')
            file_contents_string = file_pointer.read()
            file_pointer.close()
            exec(file_contents_string)

    def read_file(self):
        if self.parse():
            try:
                self.execute_file_lines()
                return True
            except:
                pass
        return False

    # TODO: remove entirely
    def remove_package_path_from_sys_modules(self, package_path):
        '''Total hack. Should be eliminated entirely.
        '''
        command = "if '{}' in sys.modules: del(sys.modules['{}'])".format(
            package_path, package_path)
        exec(command)

    def run_abjad(self, prompt=True):
        os.system('abjad {}'.format(self.filesystem_path))
        self.session.io_manager.proceed('file executed', is_interactive=prompt)

    def run_python(self, prompt=True):
        os.system('python {}'.format(self.filesystem_path))
        self.session.io_manager.proceed('file executed.', is_interactive=prompt)

    # TODO: remove entirely
    def unimport(self):
        self.remove_package_path_from_sys_modules(self.packagesystem_path)
