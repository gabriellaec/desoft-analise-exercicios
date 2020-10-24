def conta_ocorrencias(x):
    K = {}
    for palavra in x:
        if palavra in K:
            K[palavra]+= 1
        else:
            K[palavra]=1
    return K
            
    return D 

def mais_frequente(lista):  
    ocorrencias = conta_ocorrencias(lista)
    maior = 0
    maior_palavra = ""
    for palavra in ocorrencias:
        num_palavra = ocorrencias[palavra]
        if num_palavra > maior:
            maior = num_palavra
            maior_palavra = palavra
    return maior_palavra

    
    