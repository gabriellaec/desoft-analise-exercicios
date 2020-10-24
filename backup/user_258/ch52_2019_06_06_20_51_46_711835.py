def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return False
 
    for k in lista:
        if k > Maior:
            Maior = k
        if k < Maior:
            return False
    return True


