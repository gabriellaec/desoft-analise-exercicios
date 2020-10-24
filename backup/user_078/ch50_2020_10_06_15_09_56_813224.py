def junta_nome_sobrenome(nome, sobrenome):
    lista_nome_sobrenome = []
    while i < len(nome):
        novo_nome = nome[i] + ' ' + sobrenome[i]

        lista_nome_sobrenome.append(novo_nome)
    
    return lista_nome_sobrenome