def junta_nome_sobrenome(nome, sobrenome):
    nome_sobrenome = []
    i = 0
    while i < len(nome):
        name = nome[i]
        surname = sobrenome[i]
        NC = str(name) + str(surname)
        nome_sobrenome.append(NC)
        i += 1
    return nome_sobrenome
