import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import root

rho = 2000
omega = 7.27e-5
G = 6.67e-11
Me = 5.79e24
R = 6.4e6


def model(sg, x):
    return G * Me * rho / (R + x)**2 - rho * omega**2 * (R + x)


r = np.linspace(0, 2e8, 100)

fig, ax = plt.subplots()
for sigma0 in np.arange(-0.8e11, 1e11, 2e10):
    sigma = odeint(model, sigma0, r)
    print(root(sigma, 1.4e8))

    plt.plot(r, sigma / 1e9, label="$\\sigma(0)$={} GPa".format(sigma0 / 1e9))

plt.xlim((0, 2e8))
plt.ylim((0, 200))
ax.legend(loc="best")
plt.xlabel('The distance $x$ from the origin of the cable (m)')
plt.ylabel('The stress $\\sigma(x)$ in the cable (GPa)')
# plt.show()
plt.savefig(os.path.abspath(__file__ + "/../../") + "/images/stress.pdf")
