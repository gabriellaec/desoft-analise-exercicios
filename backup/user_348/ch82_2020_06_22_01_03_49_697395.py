def primeiras_ocorrencias(string):
    # Cria um dicionário onde serão adicionados os caracteres e suas ocorrências
    dicionario = {}
    # determina o índice atual
    i = 0
    # determina a condição do loop
    while i<len(string):
        # Verifica se o caracter não é uma chave do dicionário
        if string[i] not in dicionario.keys():
            # Se não for, adiciona o caracter e sua ocorrência ao dicionário
            dicionario[string[i]] = i
        i = i + 1
    return dicionario
       
        