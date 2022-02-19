import sys
sys.path.append("..")
import numpy as np
from itertools import count


class Nodes:
    index_counter = 0 
    node_index_dict = dict ()
    index = index_counter
    def __init__(self, name, phase):
        self.name = name
        self.phase = phase
        #self.index = index
        

        

        
        
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,):
        self.index = self.index_counter
        self.index_counter +=1
        self.node_index_dict[self.name]=self.index
        
        #node index is index counter + 1
        #where does this statement go
