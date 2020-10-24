def monta_mala(todospesos):
    pesomalas = []
    z = 0
    for i in range (len(todospesos)):
        z = z + todospesos[i]
        if z > 23:
            break
        pesomalas.append(todospesos[i])
    return pesomalas