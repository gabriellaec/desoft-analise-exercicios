def PiWallis(n):
    lista=[]
    for i in range(1,n):
        esquerda = float((2 * i)/(2 * i - 1))
        direita = float ((2 * i)/(2 * i + 1))
        total =  esquerda * direita
        lista.append(total)
    produto = 1
    for j in range(len(lista)):
        produto *= lista[j]
    return produto
                    
        
        
    