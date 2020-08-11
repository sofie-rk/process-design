# Ammonia lopp

from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

name = ['N2', 'H2', 'NH3', 'Ar']
n = len(name)

# stoichiometric matrix
N = np.array([ [-1], # N2
               [-3], # H2
               [2],  # NH3
               [0]   # Ar 
            ])

# conversion matrix
X_N2 = 0.30
X = np.array([[X_N2, 0, 0, 0]])

# separator factor matrix
A = np.diag([0.98, 0.99, 0, 1])

# purge split flow ration
alpha = 0.95

# flow in make-up stream [kmol/h]
F0 = np.array([240, 750, 0, 10])

def calculating_flows(alpha):
    # M = alpha * A * (I + NX)
    M = alpha * np.dot(A, np.eye(n) + np.dot(N, X))
    
    ### EQUATIONS ###
    F4 = linalg.solve(np.eye(n)-M, np.dot(M, F0)) 
    F1 = F0 + F4
    F2 = np.dot(np.eye(n) + np.dot(N, X) , F1)
    F3 = np.dot(A, F2)
    F5 = np.dot(np.eye(n)-A, F2)
    F6 = (1-alpha)*F3

    return F1, F2, F3, F4, F5, F6

F1, F2, F3, F4, F5, F6 = calculating_flows(alpha=0.95)

# recycle ratio
recyle_ratio = F4.sum() / F0.sum()

print("------------------------------------------------------------------------")
print("Alpha: ", alpha, "\tRecycle ratio: ", round(recyle_ratio,2))
print("------------------------------------------------------------------------")

print('{0:10} {1:6} {2:6} {3:6} {4:6} {5:6} {6:6} {7:6}'.format(
        "Stream", "F0", "F1", "F2", "F3", "F4", "F5", "F6"))

print("------------------------------------------------------------------------")

for i in range(n):
    print('F({0:3}) {1:6.0f} {2:6.0f} {3:6.0f} {4:6.0f} {5:6.0f} {6:6.0f} {7:6.0f}'.format(
        name[i], F0[i], F1[i], F2[i], F3[i], F4[i], F5[i], F6[i]
    ))
print("------------------------------------------------------------------------")
print()

### THE EFFECT OF SPLIT FLOW RATIO alpha ON INERT CONCENTRATION OF STREAM 1###
# changing alpha from 0.9 to 0.99
print("Observing effect of split flow ratio on inert concentration")
print('{0:15} {1:15}'.format("Alpha [-]", "Inert mole fraction [-]"))

alpha_values = np.linspace(0.9, 0.99, 30)
inert_conc = np.zeros(len(alpha_values))

for i in range(len(alpha_values)):
    F1, F2, F3, F4, F5, F6 = calculating_flows(alpha_values[i])
    inert_conc[i] = F1[-1]/F1.sum()
    print('{0:10} {1:20}'.format(round(alpha_values[i],3), round(inert_conc[i],3)))

plt.plot(alpha_values, inert_conc, label="Inert mole fraction, stream 1")
plt.xlabel("Alpha")
plt.ylabel("Mole fraction")
plt.title("Inert concentration in stream 1 as a function of split flow ratio")
plt.savefig("ammonia-loop/inert_conc_alpha.png")
plt.show()
print("------------------------------------------------------------------------")

