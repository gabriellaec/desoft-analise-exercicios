def verifica_quadrado_perfeito(n):
    m= n
    i= 0
    while (m >=0):
        if m > 0:
            m -= i*2
            i += 1
        elif m == 0:
            m-=2
    if m**2 == n**2:
        reposta= True 
    elif m**2 != n**2:
        resposta= False 
    return resposta
     