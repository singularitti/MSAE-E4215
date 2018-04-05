#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("classic")

sample = 100
s = np.array([15, 13.3, -6.3])  # s11, s44, s12
s11 = s[0]
s12 = s[2]
s44 = s[1]


def directional_factor(theta, phi):
    l1 = np.cos(phi) * np.sin(theta)
    l2 = np.sin(phi) * np.sin(theta)
    l3 = np.cos(theta)
    return l1 ** 2 * l2 ** 2 + l2 ** 2 * l3 ** 2 + l3 ** 2 * l1 ** 2


def s_average(theta, phi):
    return s11 - 2 * (s11 - s12 - s44 / 2) * directional_factor(theta, phi)


theta = np.pi * np.random.random(sample)
phi = 2 * np.pi * np.random.random(sample)

print(np.mean([np.mean([s_average(theta[i], phi[i])
                        for i in range(sample)]) for i in range(100)]))
