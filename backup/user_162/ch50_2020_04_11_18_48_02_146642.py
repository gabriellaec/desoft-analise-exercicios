def junta_nome_sobrenome(n, s):
    ns = [0]*len(n)
    i=0
    while i < len(n):
        ns[i] = n[i] +" "+ s[i]
        i+=1
    return ns