def calcula_tempo(nada):
    dic = {}
    for atleta, aceleracao in nada.items():
        tempof = (200/aceleracao)**0.5
        dic[atleta] = tempof
    return aceleracao