def aniversariantes_de_setembro (dicionário):
    # Cria um dicionário vazio onde serão adicionados os dados dos aniversariantes de setembro
    dicionário2 = {}
    # Condição 
    for nome,data in dicionário.items():
        # Verifica se o índice 4 do valor é 9
        if data[4]=='9':
            # Se for, adiciona o ítem ao dicionário de setembro
            dicionário2[nome] = data
    return dicionário2