from simuq.qsystem import QSystem
from simuq.environment import boson

# Bose-Hubbard model, based on arXiv:2209.11153
# Assuming a square lattice
n = 5 # lattice size
qs = QSystem()
bosons = [boson(qs) for i in range(N)

J = 1
U = 0.1
mu = 1
h0 = 0
for x in range(n):
    for y in range(n):
        i = y*n + x
        if x < n:
            j = i + 1 # right neighbor
            h0 += -J * (bosons[i].a * bosons[j].c + bosons[j].a * bosons[i].c)
        if y < n:
            j = i + n # upper neighbor
            h0 += -J * (bosons[i].a * bosons[j].c + bosons[j].a * bosons[i].c)

h1 = 0
h2 = 0
for i in range(n*n):
    n_hat = bosons[i].a * bosons[i].c
    h1 += U * n_hat * (n_hat-1) / 2
    h2 += -mu * n_hat


h = h0 + h1 + h2
t = 0.1
qs.add_evolution(h, t)