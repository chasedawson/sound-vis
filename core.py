# core file -- this is the file that will be run
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def reflection_of(v1, v2):
    part1 = np.dot(v1, v2)
    part2 = 2*part1
    part3 = part2*v2
    reflected_vector = v1-part3
    norm = reflected_vector/(np.linalg.norm(reflected_vector))
    return norm


def simulate_speaker():
    v_set = np.array([])
    for t in range(-10, 10, 1):
        t /= 10
        f_x = ((9/8)**2*((9/8)*math.cos((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_y = ((9/8)**2*(-(9/8)*math.sin((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_z = -1
        n = np.array([f_x, f_y, f_z])
        v = np.array([0, 3, -2])
        v_prime = reflection_of(v, n)
        print(v_set)
        print(v_prime)
        if len(v_set) == 0:
            v_set = v_prime
        else:
            v_set = np.vstack([v_set, v_prime])
    return v_set


def graph_reflections(v_set):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    vx = np.array([])
    vy = np.array([])
    vz = np.array([])
    for v in v_set:
        vx = np.append(vx, v[0])
        vy = np.append(vy, v[1])
        vz = np.append(vz, v[2])
    ax.scatter(vx, vy, vz)
    plt.show()


v_set = simulate_speaker()
print(v_set)
graph_reflections(v_set)
