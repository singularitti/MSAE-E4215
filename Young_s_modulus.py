import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 500)
s11 = 15
s12 = -6.3
s44 = 13.3


def q(t):
    return 1/4*np.cos(t)**4 + np.cos(t)**2 * np.sin(t)**2
    
    
def s11_prime(t):
    return s11 - 2 * q(t) * (s11 - s12 - s44/2)
    

def youngs(t):
    return 1 / s11_prime(t)

plt.figure()
plt.plot(theta, youngs(theta))
plt.xlim((min(theta), max(theta)))
plt.xlabel("$\\theta$", fontsize=16)
plt.ylabel("Young's modulus $E$", fontsize=16)
plt.savefig('curve.png', transparent=True)

plt.figure()
plt.polar(theta, youngs(theta))
plt.title("Young's modulus $E$", fontsize=18, va='bottom')

# plt.show()
plt.savefig('polar.png', transparent=True)
