def apaga_repetidos(texto):
    nova = ""

    for i in texto: 
        if i not in nova:
            nova = nova+i
        else:
            nova = nova+"*"
    return nova