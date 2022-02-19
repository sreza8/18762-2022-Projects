
from stringprep import in_table_c3
import numpy as np
from itertools import count
from classes.Nodes import Nodes

# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse


class Resistors:
    def __init__(self, name, from_node, to_node, r):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.r = r
        
        
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self):
        self.name=Nodes.node_index_dict[Nodes.index]
        self.from_node_index = Nodes.node_index_dict[self.from_node] 
        self.to_node_index = Nodes.node_index_dict[self.to_node]
        print (Nodes.index_counter)

        #do before assigning stamps
        #row 1 corresponds to node 1
       
        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y):
        Y[self.from_node_index,self.from_node_index]+= 1/self.r
        Y[self.from_node_index,self.to_node_index]+= -1/self.r
        Y[self.to_node_index,self.from_node_index]+= -1/self.r
        Y[self.to_node_index,self.to_node_index]+= 1/self.r
