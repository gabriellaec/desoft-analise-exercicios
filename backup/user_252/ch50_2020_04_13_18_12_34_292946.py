def junta_nome_sobrenome(n, s):
    i=0
    t=len(n)
    espaco=' '
    j=[0]*t
    while i<t:
        j[i]=n[i]+espaco+s[i]
        i+=1
    return juntos