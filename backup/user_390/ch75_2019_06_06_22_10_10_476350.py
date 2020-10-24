def verifica_primos(lista):
    dic={}
    i=2
    for p in lista:
        while i<p:
            if p<=1:
                primo=False
                dic[p]=primo
            elif p%i==0:
                primo=False
                dic[p]=primo
            else:
                primo=True
                dic[p]=primo
            i+=1
    return dic
        