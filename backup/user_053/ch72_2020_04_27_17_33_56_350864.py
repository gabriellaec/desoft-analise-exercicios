def lista_caracteres(palavra):
    caracteres = []
    for letra in palavra:
        caracteres.append(letra)
    i = 0
    while i < len(caracteres):
        j = 0
        while j < len(caracteres):
            if caracteres[i] == caracteres[j] and i != j:
                del(caracteres[j])
            j += 1
        i += 1
    return caracteres