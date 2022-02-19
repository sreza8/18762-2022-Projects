import sys
import numpy as np
from itertools import count
from classes.Nodes import Nodes
from lib.stamp import stamp_dense

def initialize(devices, size_Y, Y,J):
    #V_init=Y^-1*J
    #faster to do Y as NumPy array
    # Y = np.zeros(size_Y, size_Y)
    Y = np.zeros((size_Y, size_Y))
    J = np.zeros((size_Y,1))
    
    for elements in devices["resistors"]:
        elements.stamp_dense(Y)
    for elements in devices["capacitors"]:
        elements.stamp_open(Y, J)
    for elements in devices["inductors"]:
        elements.stamp_close(Y, J)
    for elements in devices["VoltageSources"]:
        elements.stamp_open(Y, J)
    
    # take inverse of Y and multiply by J
    V_init = np.linalg.inv(Y)*J


    return V_init