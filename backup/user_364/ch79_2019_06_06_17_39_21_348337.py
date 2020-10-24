def monta_dicionario(lista1,lista2):
    dic={}
    i=0
    while i < len(lista1):
        chave= lista1[i]
        valor=lista2[i]
        dic[chave]=valor
        i+=1
        
        return dic
    
        