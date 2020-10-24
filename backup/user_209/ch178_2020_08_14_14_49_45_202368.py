def junta_nomes(homens,mulheres,sobre):
    lista = []
    if len (homens) != 0 and len (sobre) != 0:
        for e in homens:
            for i in sobre:
                completo = e + ' '+ i
                lista.append(completo)
    if len (mulheres) != 0 and len (sobre) != 0:
        for j in mulheres:
            for k in sobre:
                completao = j + ' '+ k
                lista.append(completao)
    return lista