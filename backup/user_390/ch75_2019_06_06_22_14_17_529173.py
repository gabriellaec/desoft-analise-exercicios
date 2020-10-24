def verifica_primos(lista):
    dic={}
    i=2
    for n in lista:
        while i<n:
            if n%i==0:
                primo=False
            i+=1
        if n<=1:
            primo=False
        else:
            primo=True
 
    return dic
        