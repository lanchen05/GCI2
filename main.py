import math
from material import Material
from fusion_sim import FusionSim

# Helper function to test and print results
def assert_equal(actual, expected, test_name):
    if abs(actual - expected) < 1e-6:
        print(f"PASS: {test_name}")
    else:
        print(f"FAIL: {test_name}\nExpected: {expected}, but got: {actual}")

# Test Material getters
def test_material():
    mat = Material()
    print("Testing Material defaults...")
    assert_equal(mat.get_energy_out(), 0.0, "Energy Out Default")
    assert_equal(mat.get_burn_time(), 0.0, "Burn Time Default")
    assert_equal(mat.get_mass(), 1.0, "Mass Default")
    assert_equal(mat.get_electron_density(), 1.0, "Electron Density Default")
    assert_equal(mat.get_ion_density(), 1.0, "Ion Density Default")
    assert_equal(mat.get_temp(), 300.0, "Electron Temperature Default")

    if mat.get_material() == "Default":
        print("PASS: Material Name Default")
    else:
        print("FAIL: Material Name Default")

    if mat.is_stable():
        print("PASS: Stability Default")
    else:
        print("FAIL: Stability Default")

# Test FusionSim energy calculation
def test_fusion_sim_energy():
    mat1 = Material()
    mat2 = Material()
    sim = FusionSim(mat1, mat2)
    expected_energy = (1.0 - 1.0) * 931.5 * (299792458 ** -3)
    assert_equal(sim.energy(), expected_energy, "FusionSim Energy Calculation")

# Test FusionSim burn time calculation
def test_fusion_sim_burn_time():
    mat1 = Material()
    mat2 = Material()
    try:
        sim = FusionSim(mat1, mat2)
        burn_time = sim.burn_time()
        print(f"PASS: Burn Time Calculation: {burn_time} seconds")
    except RuntimeError as e:
        print(f"FAIL: Burn Time Calculation - {e}")

def main():
    print("Running Material and FusionSim Tests...")
    test_material()
    test_fusion_sim_energy()
    test_fusion_sim_burn_time()

if __name__ == "__main__":
    main()
