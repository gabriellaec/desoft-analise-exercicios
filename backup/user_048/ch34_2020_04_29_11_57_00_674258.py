def maior_primo_menor_que(n):
    lista=[]
    if n<=2:
        return -1
    else:
        for valor in range(n): 
            if valor > 2: 
                for i in range(2, valor//2 + 2): 
                    if (valor % i) == 0: 
                        break
                    else: 
                        if i == valor//2 + 1:
                            lista.append(valor)
                            
    return max(lista)
        