def lista_primos(n):
    i=2
    lista=[]
    while len(lista) <= n:
        primo=0
        for a in range(2,i-1):
            if i%a==0:
                primo+=1
                break
        if primo==0:
            lista.append(i)
        i+=1
    return lista
print (lista_primos(100))