#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

frequencies = np.array([27.5, 55, 110, 220, 440, 880, 1760, 3520])
Q_max = 4000 / 43
Q = np.zeros(np.size(frequencies))
tau_c = np.zeros(np.size(frequencies))

for i, frequency in enumerate(frequencies):
    Q[i] = Q_max * np.cosh(np.log(2 * np.pi * 1.89 * 10 ** -15 * frequency) + 83700 / 8.314 / 295)
    tau_c[i] = Q[i] / (np.pi * frequency)

fig, ax = plt.subplots()
ax.plot(frequencies, tau_c)
ax.scatter(frequencies, tau_c)
ax.set_xlim((min(frequencies) * 0.9, max(frequencies) * 1.1))
ax.set_xscale('log')
plt.ylim((min(tau_c) * 0.999999, max(tau_c) * 1.0000001))
max_yticks = 10
yloc = plt.MaxNLocator(max_yticks)
ax.set_xlabel("$\\ln(\\nu)$", fontsize=16)
ax.set_ylabel("$\\tau_C$", fontsize=16)
ax.set_title("Problem 8.5 (b)", fontsize=18)
# plt.show()
fig.savefig(my_path + "/images/3_b.pdf")
