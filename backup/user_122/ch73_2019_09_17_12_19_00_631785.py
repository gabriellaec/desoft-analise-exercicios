def remove_vogais(palavra):

    saida = ""
    for letra in palavra:
        if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
            saida += letra
            
    return saida