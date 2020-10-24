def conta_a (string):
    # Cria uma variável que armazenará o índice da string
    i = 0
    # Cria uma variável que armazenará o número de vezes que a letra 'a' apareceu até o momento
    contador = 0
    # Determina a condição para o loop (enquato o índice for menor que o número de elementos da string)
    while i < len(string):
        # verifica se o elemento atual da string é 'a'
        if string[i] == 'a':
            # Se for adiciona 1 ao contador
            contador = contador + 1
        i = i + 1
    return contador
        