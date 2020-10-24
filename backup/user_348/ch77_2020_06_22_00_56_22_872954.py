def calcula_tempo (atletas):
    # Cria um dicionário vazio que armazenará o tempo
    tempo = {}
    # Condição
    for nome, a in atletas.items():
        # calcula o tempo de cada atleta
        t = (200/a)**(1/2)
        # Adiciona o tempo ao valor do dicionário de tempos
        tempo[nome] = t
    return tempo