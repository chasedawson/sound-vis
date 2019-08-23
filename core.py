# core file -- this is the file that will be run
import numpy as np
import math
import plotly.graph_objects as go


def reflection_of(v1, v2):
    part1 = np.dot(v1, v2)
    part2 = 2*part1
    part3 = part2*v2
    reflected_vector = v1-part3
    norm = reflected_vector/(np.linalg.norm(reflected_vector))
    return norm


def simulate_speaker():
    v_set = np.array([])
    for t in range(-1000, 1000, 1):
        t /= 100
        f_x = ((9/8)**2*((9/8)*math.cos((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_y = ((9/8)**2*(-(9/8)*math.sin((1/4)+t)-(1/2)*math.sin((1/4)+math.pi/2+t)+math.cos((1/4)+t)))
        f_z = -1
        n = np.array([f_x, f_y, f_z])
        v = np.array([0, 3, -2])
        v_prime = reflection_of(v, n)
        if len(v_set) == 0:
            v_set = v_prime
        else:
            v_set = np.vstack([v_set, v_prime])
    return v_set


def graph_reflections(v_set):
    vx = np.array([])
    vy = np.array([])
    vz = np.array([])

    for v in v_set:
        vx = np.append(vx, v[0])
        vy = np.append(vy, v[1])
        vz = np.append(vz, v[2])


    fig = go.Figure(data=[go.Scatter3d(x=vx, y=vy, z=vz, mode='markers')])
    fig.write_html('first_figure.html', auto_open=True)

def projections(v_set):
    vx = np.array([])
    vy = np.array([])
    vz = np.array([])

    for v in v_set:
        vx = np.append(vx, v[0])
        vy = np.append(vy, v[1])
        vz = np.append(vz, v[2])

    # xy projection
    fig = go.Figure(data=go.Scatter(x=vx, y=vy))
    fig.write_html('xy_proj.html', auto_open=True)

    # xz projection
    fig = go.Figure(data=go.Scatter(x=vx, y=vz))
    fig.write_html('xz_proj.html', auto_open=True)

    # yz projection
    fig = go.Figure(data=go.Scatter(x=vy, y=vz))
    fig.write_html('yz_proj.html', auto_open=True)

v_set = simulate_speaker()
graph_reflections(v_set)
projections(v_set)
