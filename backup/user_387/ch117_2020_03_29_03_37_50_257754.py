import numpy as np

def snell_descartes(n1, n2, teta1):
    return np.arcsin(np.sin(teta1)*n1/n2)