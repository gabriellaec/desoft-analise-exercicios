def PiWallis(n):
    sequenciapares = []
    sequenciaimpares = []
    resultado = 0 
    for i in range (2, n+1):
        if i%2 == 0:
            sequenciapares.append(i)
        else:
            sequenciaimpares.append(1/i)      
    for k in range (len(sequenciapares)):
        resultado *= sequenciapares[k]*sequenciaimpares[k]
    return (resultado*2)