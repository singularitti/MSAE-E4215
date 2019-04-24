import matplotlib.pyplot as plt
import numpy as np

tau0 = 1.89e-15
temperature = 295
frequencies = [27.5, 55, 110, 220, 440, 880, 1760, 3520]


def tau(frequency):
    x = 2 * np.pi * frequency
    return np.cosh(np.log(x * tau0) + 83700 / (8.314 * temperature)) / (0.106 * x)


if __name__ == "__main__":
    y = list(map(tau, frequencies))
    diff = max(y) - min(y)
    plt.figure(figsize=(8, 6))
    plt.plot(y, 'o')
    plt.ylim((min(y) - diff / 50, max(y) + diff / 50))
    plt.xlabel("$\\ln(\\nu)$")
    plt.ylabel("$\\tau_C$")
    plt.savefig("../images/8_5.pdf")
    plt.show()
