def calcula_tempo(dicionario):
    dicionarionovo={}
    for nome, aceleracao in dicionario.items():
        dicionarionovo[nome]= ((100*2)/aceleracao)**0.5
    return dicionarionovo