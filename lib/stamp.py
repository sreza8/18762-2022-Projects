

def stamp_sparse():
    pass

def stamp_dense(devices, Y, J, N, t ):
    for elements in devices["resistors"]:
        elements.stamp_dense(Y)
    for elements in devices["capacitors"]:
        elements.stamp_dense(Y, J, N, t)
    for elements in devices["inductors"]:
        elements.stamp_dense(Y, J, t)
    for elements in devices["VoltageSources"]:
        elements.stamp_dense(Y,J,N,t)