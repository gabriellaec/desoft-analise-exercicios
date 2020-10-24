import numpy
def snell_descartes (n1, n2, teta1) :
    y = np.arcsin(n1*np.sin(teta1)/n2)*(180/np.pi)
    return y 