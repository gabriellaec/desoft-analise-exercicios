def primos_entre(a,b):
    lista=[]
    i=a
    while i<b:
        n=1
        while n<i:
        	if (i % n) == 0:
                break
            else:
                n+=1
        lista.append(i)
        i+=1
    return lista
                