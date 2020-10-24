def quantos_uns(n):
    
    n = str(n)
    resultado = 0
    
    for i in n:
        if i == '1': resultado += 1
    
    return resultado