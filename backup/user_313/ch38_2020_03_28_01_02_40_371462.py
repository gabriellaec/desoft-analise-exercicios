def quantos_uns(a):
    b = str(a)
    c = len(b)
    y = True

    indice = 0
    lista = []
    
    while y:
        if b[indice] == '1':
            lista.append(1)
        
        indice = indice + 1
        
        if(indice == c):
            y = False
            return(len(lista))