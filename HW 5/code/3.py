#!/usr/bin/env python3

import numpy as np

number_of_samples = 100
s11, s44, s12 = 15, 13.3, -6.3  # s11, s44, s12


def Q(theta, phi):
    l1 = np.cos(phi) * np.sin(theta)
    l2 = np.sin(phi) * np.sin(theta)
    l3 = np.cos(theta)
    return l1 ** 2 * l2 ** 2 + l2 ** 2 * l3 ** 2 + l3 ** 2 * l1 ** 2


def s_average(theta, phi):
    return s11 - 2 * (s11 - s12 - s44 / 2) * Q(theta, phi)


theta = np.pi * np.random.random(number_of_samples)
phi = 2 * np.pi * np.random.random(number_of_samples)

print(np.mean([np.mean([s_average(theta[i], phi[i])
                        for i in range(number_of_samples)]) for i in range(100)]))
