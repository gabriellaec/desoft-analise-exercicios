def interseccao_valores (dici1, dici2):
    listav = []
    for e in dici1.values():
        for f in dici2.values():
            if e == f and e not in listav:
                listav.append(e)
    return listav