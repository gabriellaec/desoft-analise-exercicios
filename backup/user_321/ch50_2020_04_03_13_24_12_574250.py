def junta_nome_sobrenome(n,s):
    i = 0
    lista = []
    while i <= len(n)-1:
        lista.append(n[i] + ' ' + s[i])
        i += 1
    return lista