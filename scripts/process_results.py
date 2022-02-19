from stringprep import in_table_c3
import numpy as np
from itertools import count
from classes.Nodes import Nodes
from matplotlib import pyplot

def process_results(V_waveform, devices):
    #need info for:
    # V2a and I2a which is voltage and current at node n4_a
    # V2b I2b at node n4_b
    # V2c I3c at node n4_c

    #loop for all 100 data points for time 0 to 0.2 in 0.002 increments
    for x in range (100):
        #having trouble processing results. My V_waveform stores the v vector at each time. How do I access the voltage in node n4_a
        #plot V2a
        v_vector_at_time_x = V_waveform[x]
        #trying to get index for node of interest
        index = Nodes.node_index_dict[n4_a] 
        V2a = v_vector_at_time_x[index]
        t = x*0.002
        pyplot.plot(t, V2a)

        #plot V2b
        index = Nodes.node_index_dict[n4_b] 
        V2b = v_vector_at_time_x[index]
        t = x*0.002
        pyplot.plot(t, V2b)


        #plot V2c
        index = Nodes.node_index_dict[n4_c] 
        V2c = v_vector_at_time_x[index]
        t = x*0.002
        pyplot.plot(t, V2c)

        

        #use mat plot lib


