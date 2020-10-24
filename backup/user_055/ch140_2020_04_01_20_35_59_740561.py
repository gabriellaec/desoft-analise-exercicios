def faixa_notas(notas):
    lista = []
    inf = []
    med = []
    aci = []
    x = float()
    for x in notas:
        if x < 5:
            inf.append(x)
        if x > 5 and x <= 7:
            med.append(x)
        if x > 7:
            aci.append(x)

    lista.append(len(inf))
    lista.append(len(med))
    lista.append(len(aci))
    
    return lista




