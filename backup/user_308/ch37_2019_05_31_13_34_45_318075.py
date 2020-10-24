def lista_primos(n):
    lista=[]
    for num in range (2,n):
        primo=True
        for e in range (2,n):
            if num%e==0:
                primo=False
        if primo==True:
            lista.append(num)
    return lista