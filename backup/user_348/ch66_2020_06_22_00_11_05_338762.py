def lista_sufixos (string):
    # Cria uma lista onde serão adicionados os sufixos
    lista = []
    # Cria uma variável com os índices
    i = 0
    # Determina a condição do loop
    while i < len(string):
        # Cria uma variável com o sufixo (todos os elementos depois do índice atual)
        sufixo = string[i:]
        # Adiciona o sufixo à lista de sufixos
        lista.append(sufixo)
        i = i + 1
    return lista