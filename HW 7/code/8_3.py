import matplotlib.pyplot as plt
import numpy as np

Ea = 1
Eb = 3
eta = 1
sigma0 = 10


def epsilon(t):
    if not Eb * epsilon0 <= sigma0:
        raise ValueError("Not allowed value!")
    return (Eb * epsilon0 - sigma0) / Eb * np.exp(-Ea * Eb * t / (3 * eta * (Ea + Eb))) + sigma0 / Eb


if __name__ == "__main__":
    time = np.linspace(0, 40, 100)
    for epsilon0 in np.linspace(0, 2, 5):
        plt.plot(time, epsilon(time), label="$\\varepsilon(t)$, $\\varepsilon_0 = {0}$".format(epsilon0))
    plt.plot(time, [sigma0 / Eb] * len(time), 'k-.', label="$\\frac{ \\sigma_0 }{ E_b }$")
    plt.xlim((min(time), max(time)))
    plt.xlabel("$t$")
    plt.ylabel("$\\varepsilon$")
    plt.legend(loc="best")
    plt.savefig("../images/8_3.pdf")
    plt.show()
