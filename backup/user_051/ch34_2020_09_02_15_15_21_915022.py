def maior_primo_menor_que(n):
    i=2
    lista=[]
    while i <= n:
        primo=0
        for r in range(2,i-1):
            if i%r==0:
                primo+=1
                break
        if primo==0:
            lista.append(i)
        i+=1
    if len(lista) == 0:
        return -1
    else:
        return lista[len(lista)-1]
print (maior_primo_menor_que(11))
