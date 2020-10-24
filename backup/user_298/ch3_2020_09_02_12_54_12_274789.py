π=3.1415
def calcula_gaussiana(x,μ,σ):
    result=(1/σ*(2*π**0.5))*10**(-0.5*(x-μ/σ)**2)
    return result