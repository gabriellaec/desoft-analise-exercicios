def junta_nome_sobrenome(n, s):
    i =0
    while i <= len(n):
        a= '{0} {1}'.format(n[i], s[i])
        lista= []
        lista.append(a)
        i++1
    return lista