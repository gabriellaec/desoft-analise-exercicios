def estritamente_crescente(n):
    if len(n)==0:
        return []
    else:
        i=0
        m=n[0]
        lista=[]
        while i<len(n):
            if n[i]>m:
                m = n[i]
                lista.append(n[i])
            i+=1
        return lista
        