def calcula_tempo(atletas_para_aceleração):
    atletas_para_tempodeprova = {}
    for atletas, aceleração in atletas_para_aceleração.items():
        tempo = (200/aceleração)**0.5 
        atletas_para_tempodeprova[atletas] = tempo
    return atletas_para_tempodeprova