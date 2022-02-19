import sys
sys.path.append("..")
import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class Inductors:
    def __init__(self, name, from_node, to_node, l, delta_t):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.l = l  
        self.delta_t = delta_t
        
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,):
        self.name=Nodes.node_index_dict[Nodes.index_counter]
        self.from_node_index = Nodes.node_index_dict[self.from_node] 
        self.to_node_index = Nodes.node_index_dict[self.to_node]
        Nodes.index_counter += 1
        self.current_index = Nodes.index_counter

        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y, J, t, N):

        #eq resistor
        Y[self.from_node_index,self.from_node_index]+= (self.delta_t/(2*self.l))
        Y[self.from_node_index,self.to_node_index]+= -(self.delta_t/(2*self.l))
        Y[self.to_node_index,self.from_node_index]+= -(self.delta_t/(2*self.l))
        Y[self.to_node_index,self.to_node_index]+= (self.delta_t/(2*self.l))

        
        #eq voltage source
        Y[self.current_index, self.vp_node_index] += 1
        Y[self.current_index, self.vn_node_index] += -1
        Y[self.vp_node_index, self.current_index] = 1
        Y[self.vn_node_index, self.current_index] = -1

        

        Y[self.vp_node, N+1] += 1
        Y[self.vn_node, N+1] += -1
       

        #voltage at time t
        v=(2^0.5/3^0.5)*self.amp_ph_ph_rms * np.sin( (self.frequency_hz*np.pi/180)*t+ self.phase_deg*np.pi/180)

        #admittance
        G = self.delta_t/(2*self.l)

        #stamp Veq=v(t) + (2*L)/(delta t)*i(t)
        #i(t) = v(t)*G

        J[self.current_index] += v+((2*self.l)/self.delta_t)*(v*G)
        

    def stamp_short(self,Y, N, J):
        #Y[self.from_node_index,self.from_node_index]+= 0
        #Y[self.from_node_index,self.to_node_index]+= 0
        #Y[self.to_node_index,self.from_node_index]+= 0
        #Y[self.to_node_index,self.to_node_index]+= 0

        Y[self.current_index, self.from_node_index] += 1
        Y[self.current_index, self.to_node_index] += -1
        Y[self.from_node_index, self.current_index] += 1
        Y[self.to_node_index, self.current_index] += -1

        #Voltage source is 0 in ideal situation
        
