def calcula_tempo(dados_atletas):

    resultados = dict()
    
    for nome, aceleracao in dados_atletas.items():
        acel = float(aceleracao)  # Caso as acelerações venham em strings
        tempo_gasto = math.sqrt((2*100)/acel)
        resultados[nome] = tempo_gasto
    
    return resultados