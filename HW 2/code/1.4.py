#!/usr/bin/env python3
"""
Chapter 1 Ex 4.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command

si = [625, 4.63]
cu = [315, 3.49]
ge = [360, 3.85]
sn = [200, 3.14]
ag = [215, 2.95]
au = [170, 3.81]
metals = np.array([si, cu, ge, sn, ag, au])
metals_without_outlier = np.array([si, cu, ge, sn, ag])
my_path = os.path.abspath(__file__ + "/../../")

plt.figure()
plt.scatter(metals[:, 0], np.sqrt(metals[:, 1]))
for i, atom in enumerate(["Si", "Cu", "Ge", "Sn", "Ag", "Au"]):
    plt.annotate(atom, (metals[i, 0] + 5, np.sqrt(metals[i, 1])))
fit = np.polyfit(metals_without_outlier[:, 0], np.sqrt(metals_without_outlier[:, 1]), 1)
p = np.poly1d(fit)
plt.plot(np.linspace(170, 625), list(map(p, np.linspace(170, 625))))

plt.xlabel("Debye temperature $\\theta\\ \\text{(K)}$", fontsize=16)
plt.ylabel("$\\sqrt{U}\\ \\text{(eV)}$", fontsize=16)
plt.title("$\\sqrt{U}$ as a function of $\\theta$", fontsize=18)
plt.legend(["Linear fitting $\\sqrt{{U}} = {:.2e} \\theta + {:.2f}$".format(fit[0], fit[1])], loc="best")
# plt.show()
plt.savefig(my_path + "/images/pro_1_4.png", dpi=600)
