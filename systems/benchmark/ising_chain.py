# Generate a transverse field chain Ising model
# H = J Σ_{j=1}^{n-1} Z_jZ_{j+1} + h Σ_{j=1}^n X_j

import numpy as np
from simuq.qsystem import QSystem
from simuq.environment import qubit

def GenQS(n, T, J, h) :
    qs = QSystem()
    q = [qubit(qs) for i in range(n)]
    H = 0
    for i in range(n - 1) :
        H = H + J * q[i].Z * q[i + 1].Z
    for i in range(n) :
        H = H + h * q[i].X
    qs.add_evolution(H, T)
    return qs