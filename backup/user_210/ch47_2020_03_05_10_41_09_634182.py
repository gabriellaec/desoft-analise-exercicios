def estritamente_crescente(lista):
    resp = [0]
    for c in lista:
        if c > resp[-1:][0]:
            resp.append(c)
    return resp[1:]
