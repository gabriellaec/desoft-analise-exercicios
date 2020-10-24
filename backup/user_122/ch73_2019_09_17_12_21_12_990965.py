def remove_vogais(palavra):

    vogais = ["a", "e", "i", "o", "u"]
    
    saida = ""
    for letra in palavra:
        if letra not in vogais:
            saida += letra
            
    return saida