def PiWallis(n):
    sequenciapares = []
    sequenciaimpares = []
    resultado = 1 
    for i in range (n+1):
        if i%2 == 0:
            sequenciapares.append(i)
        else:
            sequenciaimpares.append(1/i)      
    for k in range (len(sequenciapares)):
        resultado *= sequenciapares[k]*sequenciaimpares[k]
    return (resultado*2)

    
