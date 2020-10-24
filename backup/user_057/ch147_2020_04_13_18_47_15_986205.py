def mais_frequente(lista):
    dic={}
    for i in range(len(lista)):
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i]] = 1        
    N=0    
    for palavra, n in dic.items():
        if n > N:
            resposta = palavra
            N = n
    return resposta      