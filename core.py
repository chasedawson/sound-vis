# core file -- this is the file that will be run
import helpers as hp
import numpy as np

v = np.array([1, 2, -1])
n = np.array([0, -1, 1])

v_ref = hp.reflect(v, n)
print(v_ref)