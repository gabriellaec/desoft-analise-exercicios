def lista_caracteres(string):
    # cria uma lista onde os caractéres serão adicionados
    lista = []
    # Determina o índice atual
    i = 0
    # Determina a condição do loop
    while i < len(string):
        # Verifica se o elemento do índice atual (caractere) não está na lista
        if string[i] not in lista:
            # Se não estiver, adiciona o caracter à lista
            lista.append(string[i])
        i = i + 1
    return lista