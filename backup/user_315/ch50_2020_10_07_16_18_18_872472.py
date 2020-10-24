def junta_nome_sobrenome(n, s):
    t=len(n)
    i=0
    espaco=' '
    j=[0]*t
    while i < t:
        j[i]=n[i]+espaco+s[i]
        i+=1
    return j