def junta_nome_sobrenome(n, s):
    i =0
    lista= []
    while i <= len(n):
        a= '{0} {1}'.format(n[i], s[i])
        lista.append(a)
        i+=1
    return lista