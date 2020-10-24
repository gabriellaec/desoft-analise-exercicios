def PiWallis(n):
    lista=[]
    i= 1
    while i <=n:
        esquerda = float((2 * i)/(2 * i - 1))
        direita = float ((2 * i)/(2 * i + 1))
        total =  esquerda * direita
        lista.append(total)
        i+=1
    produto = 1
    for j in range(len(lista)):
        produto *= lista[j]
    return produto
                    
        
        
    