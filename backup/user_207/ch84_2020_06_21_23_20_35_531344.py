def inverte_dicionario (dicio_idades):
    new_dicio = {}
    lista_idades = []

    for idade in dicio_idades.values():
        if idade not in lista_idades:
            lista_idades.append(idade)
        
    # Obtive uma lista com todas as idades diferentes:
   
    for i in lista_idades:
        new_dicio[i] = [] # cria uma lista vazia para cada idade
        for nome, idade in dicio_idades.items():
            if idade == i: # separa cada item do dicionário pelas idades
                new_dicio[i].append(nome)

    return new_dicio
        