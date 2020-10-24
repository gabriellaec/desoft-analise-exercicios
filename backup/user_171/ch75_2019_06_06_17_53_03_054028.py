def verifica_primos(lista1):
    resultado=[]
    for i in lista1:
        primo=True
        if i<=1:
            primo=False
        for e in range(2,i):
            if i%e==0 and i!=e:
                primo=False
        resultado[i]=primo
    return resultado
  
    