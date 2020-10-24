def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    lista =[]
    while i < len(nome):
        completo = nome[i] + " " + sobrenome[i]
        lista.append(completo)
        i += 1
    return lista
