def primos_entre(a, b):
    i=a
    lista=[]
    while a <= i <= b:
        primo=0
        for r in range(2,i-1):
            if i%r==0:
                primo+=1
                break
        if primo==0:
            lista.append(i)
        i+=1
    return len(lista)