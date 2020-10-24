def lista_caracteres(palavra):
    caracteres= []
    i= 0
    while i < len(palavra):
        caracteres.append(palavra[i])
        i= i + 1
    for k in caracteres:
        n= 0
        if k== caracteres[n]:
            del(caracteres[n])
            n= n + 1
        else:
            n= n + 1
    return caracteres