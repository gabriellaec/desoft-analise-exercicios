def apaga_repetidos(texto):
    nova = ""
    texto = texto.casefold()
    for i in texto: 
        if i not in nova:
            nova = nova+i
        else:
            nova = nova+"*"
    return nova