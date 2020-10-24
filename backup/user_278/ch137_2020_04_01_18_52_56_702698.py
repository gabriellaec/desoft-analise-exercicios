def calcula_aceleracao(r,f):
    import math
    fs=f/60
    w=2*math.pi*fs
    ac=(w**2)*r
    return ac