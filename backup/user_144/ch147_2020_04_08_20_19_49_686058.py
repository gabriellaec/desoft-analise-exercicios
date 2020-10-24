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
    total = conta_ocorrencias(lista)
    maior = 0
    maior_palavra = ""
    for palavra in total:
        popu_total = total[palavra]
        if popu_total > maior:
            maior = popu_total
            maior_palavra = palavra
    return maior_palavra
    
    