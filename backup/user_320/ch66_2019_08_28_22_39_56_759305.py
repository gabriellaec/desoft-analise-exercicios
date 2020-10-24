def capitaliza(string):
    cap = []
    for letra in string:
        cap.append(letra)
    cont = 0 
    while cont < len(cap):
        if cont == 0:
            cap[cont] = cap[cont].upper()
        else:
            cap[cont] = cap[cont].lower()
        cont += 1
    cap = ''.join(cap)
    return cap