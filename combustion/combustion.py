# Combustion of natural gas

import numpy as np

# Stoichiometry array
N = np.array([ -1,     0,     0,     0,     # C1 (methane)
                0,    -1,     0,     0,     # C2 (ethane)
                0,     0,    -1,     0,     # C3 (propane)
                0,     0,     0,    -1,     # C4 (butane)
                1,     2,     3,     4,     # CO2
                2,     3,     4,     5,     # H2O
               -2,  -3.5,    -5,  -6.5,     # O2
                0,     0,     0,     0])    # N2 (inert)


# Conversion array (complete combustion)
X = np.array([  1, 0, 0, 0, 0, 0, 0, 0,     # reaction 1
                0, 1, 0, 0, 0, 0, 0, 0,     # reaction 2
                0, 0, 1, 0, 0, 0, 0, 0,     # reaction 3
                0, 0, 0, 1, 0, 0, 0, 0 ])   # reaction 4


N.shape=(8,4) # convert from array to 8x4 matrix
X.shape=(4,8) # convert from array to 4x8 matrix



# [kmol]                     C1  C2  C3  C4 CO2 H2O O2  N2
F_natural_gas = np.array([   80, 10, 5,  5,  0,  0,  0,  0])


# in reaction   1       2      3      4
O2_consumed = 80*2 + 10*3.5 + 5*5 + 5*6.5

# relation O2:N2 ia 21:79 
N2_needed = O2_consumed * 79/21

# Combustion in 20% excess air
O2_air = O2_consumed * 1.2
N2_air = N2_needed * 1.2

# [kmol]            C1  C2  C3  C4 CO2 H2O O2  N2
F_air = np.array([  0, 0, 0, 0, 0, 0, O2_air, N2_air])


F0 = F_natural_gas + F_air

R = np.eye(8) + np.dot(N, X)
F1 = np.dot(R, F0)

# Printing solution
print("Number of kilo-moles in inflow F0 and outflow F1")
print("----------------------------------------------------------------")
print("{0:16} {1:6} {2:6} {3:6} {4:6} {5:6} {6:6} {7:6} {8:6}".format(
        " ", "C1", "C2", "C3", "C4", "CO2", "H2O", "O2", "N2"
    ))
print("{0:12} {1:6.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(
    "Natural gas", F_natural_gas[0], F_natural_gas[1], F_natural_gas[2], F_natural_gas[3], F_natural_gas[4], F_natural_gas[5], F_natural_gas[6], F_natural_gas[7]
    ))
print("{0:12} {1:6.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(
    "Air", F_air[0], F_air[1], F_air[2], F_air[3], F_air[4], F_air[5], F_air[6], F_air[7]
    ))

print("{0:12} {1:6.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(
    "F0", F0[0], F0[1], F0[2], F0[3], F0[4], F0[5], F0[6], F0[7]
    ))
print("{0:12} {1:6.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(
    "F1", F1[0], F1[1], F1[2], F1[3], F1[4], F1[5], F1[6], F1[7]
    ))

    



