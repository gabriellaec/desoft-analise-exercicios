def junta_nome_sobrenome(n, s):
    i = 0
    nome_completo = []
    while i < len(n):
        nome_completo.append("{0} {1}".format(n[i], s[i]))
        i += 1
                             
    return nome_completo
        