import numpy as np
from lib.stamp import stamp_dense

def run_time_domain_simulation(devices, V_init, size_Y, SETTINGS):
    #initialize an array which will have that contains time domain waveforms of all state variables
    V_waveform = np.zeros(100)
    V_waveform[0]= V_init
    Y = np.zeros((size_Y, size_Y))
    J = np.zeros((size_Y,1))

    for t in range(0.002,0.2,0.002):
        stamp_dense(devices, Y, J, size_Y, t )
        #V_waveform[t] stores v at time t
        V_waveform[t] = np.linalg.inv(Y)*J
     
    return V_waveform