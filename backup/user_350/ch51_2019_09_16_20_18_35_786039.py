def estritamente_crescente(n):
    i=0
    m=n[0]
    lista=[]
    while i<len(n):
        if n[i]>m:
            lista.append(n[i])
        i+=1
            
        