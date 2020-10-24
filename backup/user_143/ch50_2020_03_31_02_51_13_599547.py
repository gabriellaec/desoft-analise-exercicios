def junta_nome_sobrenome(n, s):
    i=0
    st=' '
    while i<len(n):
        p=n[i]
        a=s[i]
        c=p+st+a
        i+=1
    return c
    