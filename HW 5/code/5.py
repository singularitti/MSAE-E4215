#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")


def c_prime(n, u, theta):
    """
    For a cubic material, matrix stiffness c=[c11,c44,c12],
    find the stiffness in the c_prime direction (on crystal axes), in plane with normal n,
    single in-plane direction u, angle theta CCW from u (about plane normal).
    :param n: Normal of wanted plane.
    :param u: In-plane direction on wanted plane.
    :param theta: Angle from u vector on the wanted plane.
    :return: New compliance tensor.
    """
    cc = np.array([169, 75.3, 122])
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

    c = np.zeros((3, 3, 3, 3))  # Compliance tensor

    c[0, 0, 0, 0] = cc[0]
    c[1, 1, 1, 1] = cc[0]
    c[2, 2, 2, 2] = cc[0]

    c[0, 0, 1, 1] = cc[2]
    c[1, 1, 2, 2] = cc[2]
    c[2, 2, 0, 0] = cc[2]

    c[1, 1, 0, 0] = cc[2]
    c[2, 2, 1, 1] = cc[2]
    c[0, 0, 2, 2] = cc[2]

    c[0, 1, 0, 1] = cc[1]
    c[1, 2, 1, 2] = cc[1]
    c[2, 0, 2, 0] = cc[1]

    c[1, 0, 1, 0] = cc[1]
    c[2, 1, 2, 1] = cc[1]
    c[0, 2, 0, 2] = cc[1]

    c[0, 1, 1, 0] = cc[1]
    c[1, 2, 2, 1] = cc[1]
    c[2, 0, 0, 2] = cc[1]

    c[1, 0, 0, 1] = cc[1]
    c[2, 1, 1, 2] = cc[1]
    c[0, 2, 2, 0] = cc[1]

    return np.einsum('im,jn,ko,lp,mnop', a, a, a, a, c)


def draw_on_plane(n, u):
    t = np.linspace(0, 2. * np.pi, num=360)
    s = np.array([c_prime(n, u, tt)[0, 0, 0, 0] for tt in t])
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set_xlim((min(t), max(t)))
    ax.set_ylim((min(s) - 0.5, max(s) + 0.5))
    ax.set_xlabel("Angle $\\theta$", size=16)
    ax.set_ylabel("Stiffness $c'_{1111}$", size=16)
    ax.set_title("On " + str(tuple(n)) + " plane", fontsize=18)
    new_label = np.array(np.linspace(0, 2 * np.pi, 5))
    ax.set_xticks(new_label)
    ax.set_xticklabels(["$0$", "$\\frac{\pi}{2}$",
                        "$\\pi$", "$\\frac{3\pi}{2}$", "$2\\pi$"])
    return fig


# plt.show(draw_on_plane(np.array([1, 1, 0]), np.array([-1, 1, 0])))
plt.show(draw_on_plane(np.array([1, 0, 0]), np.array([0, 1, 0])))
plt.show(draw_on_plane(np.array(np.array([1, 1, 1])), np.array([1, -1, 0])))
# draw_on_plane(np.array([1, 0, 0]), np.array([0, 1, 0])).savefig(my_path + "/images/pro_5_1.pdf")  # (1 1 0) plane
# draw_on_plane(np.array(np.array([1, 1, 1])), np.array([1, -1, 0])).savefig(
#     my_path + "/images/pro_5_2.pdf")  # (1 1 1) plane
