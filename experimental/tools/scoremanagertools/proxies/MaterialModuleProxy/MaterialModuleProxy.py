from experimental.tools.scoremanagertools.proxies.ModuleProxy import ModuleProxy


class MaterialModuleProxy(ModuleProxy):

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def material_package_name(self):
        return self.packagesystem_path.split('.')[-2]

    @property
    def material_package_path(self):
        return self.parent_package_path

    @property
    def space_delimited_material_package_name(self):
        return self.material_package_name.replace('_', ' ')

    ### PUBLIC METHODS ###

    def unimport_material_package(self):
        self.remove_package_path_from_sys_modules(self.material_package_path)

    def unimport_materials_package(self):
        self.remove_package_path_from_sys_modules(
            self._session.current_materials_package_path)
