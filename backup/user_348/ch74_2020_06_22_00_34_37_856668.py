def conta_bigramas(string):
    # Cria um dicionário onde serão adicionados o número de ocorrências
    dicionário = {}
    #Determina o loop
    for i in range(len(string)-1):
        # Define uma variável com o bigrama
        bigrama = string[i] + string[i + 1]
        # Verifica se o bigrama não é uma chave do dicionário
        if not bigrama in dicionário:
            # Se não for, cria a chave e define seu valor como 1
            dicionário[bigrama] = 1
        else:
            # se for, adiciona 1 ao valor
            dicionário[bigrama] = dicionário[bigrama] + 1
    return dicionário
        