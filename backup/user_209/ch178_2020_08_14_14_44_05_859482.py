def junta_nomes(homens,mulheres,sobre):
    lista = []
    i = 0
    for e in homens,mulheres,sobre:
        lista.append(homens[i]+sobre[i])
        lista.append(mulheres[i]+sobre[i])
    i+=1
    return lista