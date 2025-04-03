class Material:
    def __init__(self, stable=True, name="Default", mass=1.0, electron_density=1.0, ion_density=1.0, electron_temp=300.0):
        self._material = name
        self._stable = stable
        self._mass = mass
        self._electron_density = electron_density
        self._ion_density = ion_density
        self._electron_temp = electron_temp

    def get_material(self):
        return self._material

    def is_stable(self):
        return self._stable

    def get_mass(self):
        return self._mass

    def get_ion_density(self):
        return self._ion_density

    def get_temp(self):
        return self._electron_temp

    def get_electron_density(self):
        return self._electron_density
