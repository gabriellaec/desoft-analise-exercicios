import numpy
def medias_por_iniciais(dict):
    novo_d = {}
    for k,v in dict.items():
        if k[0] not in novo_d:
            novo_d[k[0]] = [v]
        else:
            novo_d[k[0]].append(v)
    for k, v in novo_d.items():
        x = numpy.mean(v)
        novo_d[k] = x
        return novo_d