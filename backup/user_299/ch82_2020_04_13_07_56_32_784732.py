def  primeiras_ocorrencias(string):
    caracteres = []
    dicii = {}
    for i, e in enumerate(string):
        if e not in caracteres:
            caracteres.append(e)
            dicii[e]=i
    return dicii