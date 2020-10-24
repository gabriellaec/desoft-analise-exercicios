def PiWallis(n):
    termo = [0]*n
    termo[0] = 2
    i = 0
    while i < n:
        if i%2 == 0:
            termo[i] = (i + 2)/ (i + 1)
        else:
            termo[i] = (i + 1)/ (i +2)

        i += 1
    
    resultado = 2

    for numero in termo:
        resultado *= numero

    return resultado
        
       
        