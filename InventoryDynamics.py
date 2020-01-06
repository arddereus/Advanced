import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from numba import njit, jitclass, float64, prange

firm_data = [('s', float64), ('S', float64), ('mu', float64), ('sigma', float64)]

@jitclass(firm_data)
class Firm:

    def __init__(self, s=10, S=100, mu=1.0, sigma=0.5):
        self.s, self.S, self.mu, self.sigma = s, S, mu, sigma

    def update(self, x):
        Z = np.random.randn()
        D = np.exp(self.mu + self.sigma * Z)
        if x <= self.s:
            return max(self.S - D, 0)
        else:
            return max(x - D,0)

    def sim_inventory_path(self, x_init, sim_length):
        X = np.empty(sim_length)
        X[0] = x_init
        for t in range(sim_length-1):
            X[t+1] = self.update(X[t])
        return X

firm = Firm()

s,S = firm.s, firm.S
sim_length = 100
x_init = 50

X = firm.sim_inventory_path(x_init, sim_length)

fig, ax = plt.subplots()
bbox = (0., 1.02, 1., .102)
legend_args = {'ncol':3, 'bbox_to_anchor': bbox, 'loc': 3, 'mode': 'expand'}

# ax.plot(X, label="inventory")
ax.plot(s * np.ones(sim_length), 'k--', label='$s$')
ax.plot(S * np.ones(sim_length), 'k-', label='$S$')
ax.set_ylim(0,S+10)
ax.legend(**legend_args)

for i in range(200):
    X = firm.sim_inventory_path(x_init, sim_length)
    ax.plot(X, 'b', alpha=0.2, lw = 0.5)

plt.show()