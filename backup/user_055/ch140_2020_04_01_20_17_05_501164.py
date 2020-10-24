def faixa_notas(notas):
    lista = []
    for x in notas:
        if x < 5:
            inferior = []
            inferior.append(x)
            lista.append(len(inferior))
        if x > 5 and x > 7:
            media = []
            media.append(x)
            lista.append(len(media))
        if x > 7:
            cabeca = []
            cabeca.append(x)
            lista.append(len(cabeca))
    return lista
     