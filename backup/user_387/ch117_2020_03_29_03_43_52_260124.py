import numpy as np

def snell_descartes(n1, n2, teta1):
    teta2 = np.arcsin(np.sin(teta1)*n1/n2)
    teta2 = teta2*(180/np.pi)
    return teta2