def pos_arroba(email):
    # Cria uma variável com o índice
    i = 0
    # Determina a condição do loop
    while i < len(email):
        # Verifica se o elemento do índice atual é igual a '@'
        if email[i] == '@':
            # Se for, retorna o número do índice
            return i
        i = i + 1
            