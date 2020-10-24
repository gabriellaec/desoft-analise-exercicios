def primos_entre(a,b):
    lista=[]
    i=a
    while i<b:
        n=1
        primo=True
        while n<i:
        	if (i % n) == 0:
                primo=False
            else:
                n+=1
        if primo:
        	lista.append(i)
            i+=1
        i+=1
    return lista
                