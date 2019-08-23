# helper file -- will contain helper functions
import numpy as np

def reflect(v, n):
    proj_v_on_n = (np.dot(v, n) / np.linalg.norm(n)**2) * n
    proj_v_on_plane = v - proj_v_on_n
    v_ref = -1 * proj_v_on_n + proj_v_on_plane
    return v_ref