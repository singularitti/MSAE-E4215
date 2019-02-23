import os

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-2*np.pi, 2*np.pi, 500)

plt.plot(t, np.sin(2 * t) / 2)
plt.xlim((min(t), max(t)))
plt.ylim((-0.5, 0.5))
plt.xlabel("$\\theta$")
plt.ylabel("$\\sigma_{\\alpha, \\beta}'$")
# plt.show()
plt.savefig(os.path.abspath(__file__ + "/../../") + "/images/sin.pdf")
