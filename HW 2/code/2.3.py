#!/usr/bin/env python3
"""
Chapter 2 Ex 3.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")

rho = 2000
w = 2 * np.pi / 24 / 3600
G = 6.67e-11
Me = 5.79e24
R = 6.4e6
xx = np.linspace(0, 22.11 * R, num=500)
my_path = os.path.abspath(__file__ + "/../../")


def sigma(x):
    C = rho * w**2 / 2 * R**2 + G * Me * rho / R
    return -rho * w**2 / 2 * (R + x)**2 - G * Me * rho / (R + x) + C


sg = [sigma(x) for x in xx]

plt.figure()
plt.plot(xx, sg)
plt.plot([3.54e7, 3.54e7], [0, np.max(sg) * 1.05], 'r-')
plt.plot([0, np.max(xx)], [sigma(3.54e7), sigma(3.54e7)], 'r-')
plt.xlim((0, np.max(xx)))
plt.ylim((0, np.max(sg) * 1.05))
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$\\sigma$", fontsize=16)
plt.title("$\\sigma$ as a function of $x$", fontsize=18)
# plt.show()
plt.savefig(my_path + "/images/pro_2.3.png", dpi=400)
