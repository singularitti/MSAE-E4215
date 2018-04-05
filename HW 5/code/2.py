#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")


def s_prime(n, u, theta):
    """
    For a cubic material, matrix compliance s=[s11,s44,s12],
    find the compliance in the s_prime direction (on crystal axes), in plane with normal n,
    single in-plane direction u, angle theta CCW from u (about plane normal).
    :param n: Normal of wanted plane.
    :param u: In-plane direction on wanted plane.
    :param theta: Angle from u vector on the wanted plane.
    :return: New compliance tensor.
    """
    ss = np.array([15, 13.3, -6.3])
    n_normalized = n / np.linalg.norm(n)  # n vector
    u_normalized = u / np.linalg.norm(u)  # u vector
    v = np.cross(n_normalized, u_normalized)  # v vector

    # New basis
    l = np.cos(theta) * u_normalized + np.sin(theta) * v  # l vector
    v_prime = np.cross(n_normalized, l)

    # Cartesian coordinates
    old_coords = np.array([[1., 0., 0.], [0, 1., 0], [0, 0, 1.]])
    new_coords = np.array([l, v_prime, n_normalized])

    a = np.dot(new_coords, old_coords)  # Coordinate transformation

    s = np.zeros((3, 3, 3, 3))  # Compliance tensor

    s[0, 0, 0, 0] = ss[0]
    s[1, 1, 1, 1] = ss[0]
    s[2, 2, 2, 2] = ss[0]

    s[0, 0, 1, 1] = ss[2]
    s[1, 1, 2, 2] = ss[2]
    s[2, 2, 0, 0] = ss[2]

    s[1, 1, 0, 0] = ss[2]
    s[2, 2, 1, 1] = ss[2]
    s[0, 0, 2, 2] = ss[2]

    s[0, 1, 0, 1] = ss[1] / 4.
    s[1, 2, 1, 2] = ss[1] / 4.
    s[2, 0, 2, 0] = ss[1] / 4.

    s[1, 0, 1, 0] = ss[1] / 4.
    s[2, 1, 2, 1] = ss[1] / 4.
    s[0, 2, 0, 2] = ss[1] / 4.

    s[0, 1, 1, 0] = ss[1] / 4.
    s[1, 2, 2, 1] = ss[1] / 4.
    s[2, 0, 0, 2] = ss[1] / 4.

    s[1, 0, 0, 1] = ss[1] / 4.
    s[2, 1, 1, 2] = ss[1] / 4.
    s[0, 2, 2, 0] = ss[1] / 4.

    return np.einsum('im,jn,ko,lp,mnop', a, a, a, a, s)


def draw_on_plane(n, u):
    t = np.linspace(0, 2. * np.pi, num=360)
    s = np.array([s_prime(n, u, tt)[0, 0, 0, 0] for tt in t])
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set_xlim((min(t), max(t)))
    ax.set_ylim((min(s) - 0.5, max(s) + 0.5))
    ax.set_xlabel("Angle $\\theta$", size=16)
    ax.set_ylabel("Compliance $s'_{1111}$", size=16)
    ax.set_title("On " + str(n) + " plane", fontsize=18)
    new_label = np.array(np.linspace(0, 2 * np.pi, 5))
    ax.set_xticks(new_label)
    ax.set_xticklabels(["$0$", "$\\frac{\pi}{2}$",
                        "$\\pi$", "$\\frac{3\pi}{2}$", "$2\\pi$"])
    return fig


# plt.show(draw_on_plane(np.array([1, 1, 0]), np.array([-1, 1, 0])))
draw_on_plane(np.array([1, 0, 0]), np.array([0, 1, 0])).savefig(my_path + "/images/pro_2_1.pdf")  # (1 1 0) plane
draw_on_plane(np.array(np.array([1, 1, 1])), np.array([1, -1, 0])).savefig(
    my_path + "/images/pro_2_2.pdf")  # (1 1 1) plane
