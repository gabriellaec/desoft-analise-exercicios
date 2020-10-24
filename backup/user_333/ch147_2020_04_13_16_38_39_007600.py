def conta_ocorrencias(lista):
    dic = {}
    palavras=[]
    valores=[]
    for i in range(len(lista)):
        if lista[i] not in palavras:
            palavras.append(lista[i])
            valores.append(1)
        else:
            for e in range(len(palavras)):
                if lista[i]==palavras[e]:
                    valores[e]+=1
    for j in range(len(palavras)):
        dic[palavras[j]]=valores[j]
    return dic
    
                
def mais_frequente(lista):
    dic=conta_ocorrencias(lista)
    maior_valor=0
    for palavra_e_valor in dic.intems():
        palavra=palavra_e_valor[0]
        valor=int(palavra_e_valor[1])
        if valor > maior_valor:
            maior_valor=valor
            mais_frequente=palavra
    return mais_frequente
        
        
        
    