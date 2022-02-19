import numpy as np
from itertools import count
from classes.Nodes import Nodes
#from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class Capacitors:
    def __init__(self, name, from_node, to_node, c, delta_t):
        self.name = name
        self.c = c
        self.from_node = from_node
        self.to_node = to_node
        self.delta_t = delta_t
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,):
        self.name=Nodes.node_index_dict[Nodes.index_counter]
        self.from_node_index = Nodes.node_index_dict[self.from_node] 
        self.to_node_index = Nodes.node_index_dict[self.to_node]
        Nodes.index_counter += 1
        self.current_index = Nodes.index_counter

        #add in extra row and column 
        Nodes.index_counter =+ 1
        print (Nodes.index_counter)

        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y,J,N, t):
        #eq resistor
        Y[self.from_node_index,self.from_node_index]+= 1/(self.delta_t/(2*self.c))
        Y[self.from_node_index,self.to_node_index]+= -1/(self.delta_t/(2*self.c))
        Y[self.to_node_index,self.from_node_index]+= -1/(self.delta_t/(2*self.c))
        Y[self.to_node_index,self.to_node_index]+= 1/(self.delta_t/(2*self.c))

        #eq voltage source
        Y[self.current_index, self.from_node_index] += 1
        Y[self.current_index, self.to_node_index] += -1
        Y[self.from_node_index, self.current_index] += 1
        Y[self.to_node_index, self.current_index] += -1
        

        J[self.current_index] += (2^0.5/3^0.5)*self.amp_ph_ph_rms * np.sin( (self.frequency_hz*np.pi/180)*t+ self.phase_deg*np.pi/180)


    def stamp_open(self,Y, J, N):
        Y[self.from_node_index,self.from_node_index]+= np.Infinity
        Y[self.from_node_index,self.to_node_index]+= np.Infinity
        Y[self.to_node_index,self.from_node_index]+= np.Infinity
        Y[self.to_node_index,self.to_node_index]+= np.Infinity

        Y[self.current_index, self.from_node_index] += 1
        Y[self.current_index, self.to_node_index] += -1
        Y[self.from_node_index, self.current_index] += 1
        Y[self.to_node_index, self.current_index] += -1
        
        #voltage source is 0
      