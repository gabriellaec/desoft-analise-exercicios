def soma_impares(números):
    # Define o valor inicial da variável que terá a soma
    soma = 0
    i = 0
    # Define a condição para o loop
    while i < len(números):
        # Verifica se o elemento que está naquele índice é ímpar
        if números[i]%2 != 0:
            # Se for ímpar adiciona o elemento ao valor total da soma
            soma = soma + números[i]
        i = i + 1
    return soma 