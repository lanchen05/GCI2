class QValue:
    amu_to_mev = 931.5  # Conversion factor from amu to MeV

    def __init__(self, init_mass=0.0, final_mass=0.0):
        self.mass_initial = init_mass
        self.mass_final = final_mass

    def calculate_q_value(self):
        return (self.mass_initial - self.mass_final) * self.amu_to_mev

    def is_exothermic(self):
        return self.calculate_q_value() > 0

    def is_endothermic(self):
        return self.calculate_q_value() < 0