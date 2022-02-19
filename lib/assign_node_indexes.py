from classes.Nodes import Nodes

def assign_node_indexes(devices):
    # loop through all devices and assign nodes
    for elements in devices["nodes"]:
        # go through all nodes in node list
        elements.assign_node_indexes()
    for elements in devices["resistors"]:
        elements.assign_node_indexes()
    for elements in devices["capacitors"]:
        elements.assign_node_indexes()
    for elements in devices["inductors"]:
        elements.assign_node_indexes()
    for elements in devices["VoltageSources"]:
        elements.assign_node_indexes()


    
    # TODO
    #should the +1 be there
    return Nodes.index_counter+1