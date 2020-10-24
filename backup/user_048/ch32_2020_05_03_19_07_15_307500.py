def lista_primos(n):
    lista=[2]
    if n<2:
        return -1
    else:
        for valor in range(n+1): 
            if valor > 1: 
                for i in range(2, valor//2 + 2): 
                    if (valor % i) == 0: 
                        break
                    else: 
                        if i == valor//2 + 1:
                            lista.append(valor)
                            
    return lista