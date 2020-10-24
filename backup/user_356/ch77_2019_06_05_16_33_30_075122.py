def calcula_tempo(dicio):
    novo={}
    for k,v in dicio.items():
        t=(200/v)**0.5
        novo[k]=t
    return novo