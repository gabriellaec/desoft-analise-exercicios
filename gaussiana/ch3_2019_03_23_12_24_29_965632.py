from matplotlib import pyplot as mp
import numpy as np

def calcula_gaussiana(x, mu, sig):
    gaussiana=np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    return gaussiana