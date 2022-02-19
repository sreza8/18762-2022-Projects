import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class VoltageSources:
    def __init__(self, name, vp_node, vn_node, amp_ph_ph_rms, phase_deg, frequency_hz):
        self.name = name
        self.vp_node = vp_node
        self.vn_node = vn_node
        self.amp_ph_ph_rms = amp_ph_ph_rms
        self.phase_deg = phase_deg
        self.frequency_hz = frequency_hz
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,):
        # get Vp node index
        # get Vn node index
        # incremend for current 
        self.vp_node_index = Nodes.node_index_dict[self.vp_node] 
        self.vn_node_index = Nodes.node_index_dict[self.vn_node]
        Nodes.index_counter += 1
        self.current_index = Nodes.index_counter

    

        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y,J,N,t):
        Y[self.current_index, self.vp_node_index] += 1
        Y[self.current_index, self.vn_node_index] += -1
        Y[self.vp_node_index, self.current_index] = 1
        Y[self.vn_node_index, self.current_index] = -1


        Y[self.vp_node, N+1] += 1
        Y[self.vn_node, N+1] += -1
        

       
        
        J[self.current_index] = (2^0.5/3^0.5)*self.amp_ph_ph_rms * np.sin(  2 * np.pi * (self.frequency_hz*np.pi/180)) + self.phase_deg*np.pi/180

        

    def stamp_open(self, Y):
        Y[self.from_node_index,self.from_node_index]+= np.Infinity
        Y[self.from_node_index,self.to_node_index]+= np.Infinity
        Y[self.to_node_index,self.from_node_index]+= np.Infinity
        Y[self.to_node_index,self.to_node_index]+= np.Infinity
        
