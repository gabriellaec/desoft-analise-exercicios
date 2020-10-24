def conta_ocorrencias(lista):
    dic={}
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic            
        
def mais_frequente(lista):
    a=conta_ocorrencias(lista)
    for i in a:
        return a
        

        