def verifica_primos(lista):
    dic={}
    i=2
    for p in lista:
        while i<p:
            if p<=1:
                dic[p]=False
            elif p%i==0:
                dic[p]=False
            else:
                dic[p]=True
            i+=1
    return dic
        