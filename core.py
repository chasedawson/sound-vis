# core file -- this is the file that will be run
import numpy as np
import math


def reflection_of(v1, v2):
    part1 = np.dot(v1, v2)
    part2 = 2*part1
    part3 = part2*v2
    reflected_vector = v1-part3
    norm = reflected_vector/(np.linalg.norm(reflected_vector))
    return norm


def simulate_speaker():
    for t in range(-10, 10, 1):
        t /= 10
        f_x = ((9/8)**2*((9/8)*math.cos((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_y = ((9/8)**2*(-(9/8)*math.sin((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_z = -1
        n = np.array([f_x, f_y, f_z])
        v = np.array([0, 3, -2])
        v_prime = reflection_of(v, n)
        print(v_prime)
        print(np.linalg.norm(v_prime))
