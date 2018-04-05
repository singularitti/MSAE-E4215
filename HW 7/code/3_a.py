#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images/"):
    os.makedirs(my_path + "/images/")

frequencies = np.array([27.5, 55, 110, 220, 440, 880, 1760, 3520])
Q_inv = 6.2e-5
tau_c = np.zeros(np.size(frequencies))

for i, frequency in enumerate(frequencies):
    tau_c[i] = 1 / (np.pi * frequency * Q_inv)

fig, ax = plt.subplots()
ax.scatter(frequencies, tau_c)
ax.plot(frequencies, tau_c)
ax.set_xlim((min(frequencies) * 0.9, max(frequencies) * 1.1))
ax.set_xscale('log')
plt.ylim((min(tau_c), max(tau_c)))
max_yticks = 10
yloc = plt.MaxNLocator(max_yticks)
ax.yaxis.set_major_locator(yloc)
ax.set_xlabel("$\\ln(\\nu)$", fontsize=16)
ax.set_ylabel("$\\tau_C$", fontsize=16)
ax.set_title("Problem 8.5 (a)", fontsize=18)
# plt.show()
fig.savefig(my_path + "/images/3_a.pdf")
