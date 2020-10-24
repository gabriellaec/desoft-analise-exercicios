def monta_dicionario(lista1,lista2):
    dic={}
    i=0
    while i<= len(lista1):
        for a in lista1:
            dic[a]= lista2[i]
            i=i+1
            return dic
    
  
        