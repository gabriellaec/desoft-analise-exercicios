def calcula_tempo (dic):
    dicnovo = {}
    for atleta,aceleracao in dic.items():
        tempo = (200/aceleracao)**0.5
        dicnovo[atleta] = t
    return dicnovo