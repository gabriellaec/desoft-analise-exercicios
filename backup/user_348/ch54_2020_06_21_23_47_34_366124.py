def calcula_fibonacci(n):
    # Verifica se o número é 1
    if n ==1:
        fibonacci = [1]
    # Se o número não for 1
    else:
        # Cria uma lista com os dois primeiros elementos da sequência
        fibonacci = [1,1]
        # Como já tem dois elementos o primeiro índice a ser analisado será o 2
        i = 2
        # Determina a condição do loop (enquanto o índice for menor que o número de elementos da sequência)
        while i < n:
            # Cria uma variável com o número que deve ser adicionado à sequência
            numero = fibonacci[i-1] + fibonacci[i-2]
            # Adiciona o número à lista
            fibonacci.append(numero)
            i = i + 1
    return fibonacci
        