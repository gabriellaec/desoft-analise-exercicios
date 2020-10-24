def junta_nome_sobrenome(n, s):
    t=len(n)
    espaco=' '
    j=[0]*t
    for i in t:
        j[i]=n[i]+espaco+s[i]
    return j