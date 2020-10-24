def remove_vogais (string):
    # Cria uma string vazia para a saída
    saida = ''
    # determina o intervalo do loop
    for i in range(len(string)):
        # Verifica se o elemento do índice atual não é uma vogal
        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
            # Se não for, adiciona o caractere atual à string de saída
            saida = saida + string[i]
    return saida
        