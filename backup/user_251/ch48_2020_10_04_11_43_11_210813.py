def eh_crescente(a):
    i = 0
    resultado = True
    while i < len(a):
        if a[i+1] > a[i]:
            resultado = True
        else:
            resultado = False
    return resultado
        
     