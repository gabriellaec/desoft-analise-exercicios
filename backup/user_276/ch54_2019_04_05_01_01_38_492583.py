def junta_nome_sobrenome(nomes, sobrenomes):
    i = 0
    nome = []
    sobrenome = []
    lista = []
    while i < len(nome) and i < len(sobrenome):
        nome_completo = nome[i] + ' ' + sobrenome[i]
        lista.append(nome_completo)
    return nome_completo   