def quantos_uns(n):
    numero = str(n)
    contagem = 0    
    i = 0
    while i < len(numero):
        if numero[i] == "1":
            i += 1
            contagem += 1
        
        else:
            i += 1
                   
    return contagem
    