def junta_nome_sobrenome(n,s):
    i = 1
    ns = []
    while i <= len(n):
        ns.append(n[i] + ' ' + s[i])
        i += 1
    return ns