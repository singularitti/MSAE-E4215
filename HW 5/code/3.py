#!/usr/bin/env python3 -u -i

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rv_continuous

s11, s44, s12 = 15, 13.3, -6.3  # s11, s44, s12


def reuss_average(s11, s12, s44):
    return (3 * s11 + 2 * s12 + s44) / 5


class SinusodialDistributionGenerator(rv_continuous):
    def _pdf(self, x):
        return np.sin(x)


def Q(theta, phi):
    l1 = np.cos(phi) * np.sin(theta)
    l2 = np.sin(phi) * np.sin(theta)
    l3 = np.cos(theta)
    return l1 ** 2 * l2 ** 2 + l2 ** 2 * l3 ** 2 + l3 ** 2 * l1 ** 2


def s_average(theta, phi):
    return s11 - 2 * (s11 - s12 - s44 / 2) * Q(theta, phi)


mc_results = []
number_of_samples = range(100, 1000, 10)
rng = SinusodialDistributionGenerator(a=0, b=np.pi)
for n in number_of_samples:
    theta = rng.rvs(size=n)
    phi = 2 * np.pi * np.random.random(n)
    mc_results.append(np.mean([s_average(theta[i], phi[i])
                               for i in range(n)]))
    # mc_results.append(np.mean([Q(theta[i], phi[i]) for i in range(n)]))
plt.plot(number_of_samples, mc_results, label="Monte Carlo sampling average")
plt.plot(number_of_samples, [reuss_average(
    s11, s12, s44)] * len(number_of_samples), label="analytical Reuss average")
plt.legend(loc="best")
plt.xlabel("Number of random numbers")
plt.ylabel("$\\bar{s}_{1111}$")
plt.title("Monte Carlo sampling VS analytical result")
# plt.show()
plt.savefig("mc_reuss.pdf")
