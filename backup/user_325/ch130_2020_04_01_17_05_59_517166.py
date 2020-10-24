def monta_mala(pesos):
    z=0
    i = 0
    while i < len(pesos):
        z+=pesos[i]
        if z>23:
            pesos=pesos[:i]
            break
        i += 1
    return pesos