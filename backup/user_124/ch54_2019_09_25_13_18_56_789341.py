def junta_nome_sobrenome(nome, sobrenome):
    nome = []
    sobrenome = []
    lista_completa = []
    i = 0 
    while i < len(nome) and i < len(sobrenome):
        nome_completo = nome[i] + sobrenome[i]
        lista_completa.append(nome_completo)
        i += 1
    return lista_completa
        