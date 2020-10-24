def primos_entre(a,b):
    lista=[]
    for num in range (a,b):
        primo=True
        for e in range (2,b):
            if num%e==0:
                primo=False
        if primo==True:
            lista.append(num)
    return len(lista)