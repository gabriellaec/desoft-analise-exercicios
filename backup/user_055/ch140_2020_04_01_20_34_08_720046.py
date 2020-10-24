def faixa_notas(notas):
    lista = []
    inf = []
    med = []
    aci = []
    for x in notas:
        if x < 5:
            inferior.append(x)
        if x > 5 and x < 7:
            media.append(x)
        if x > 7:
            acima.append(x)

    lista.append(len(inf))
    lista.append(len(med))
    lista.append(len(aci))
    
    return lista




