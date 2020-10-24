def junta_nome_sobrenome(n, s):
    i=0
    st=' '
    lista=[]
    while i<len(n):
        p=n[i]
        a=s[i]
        c=p+st+a
        lista.append(c)
        i+=1
    return lista
    