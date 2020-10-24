def remove_vogais(palavra):
    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letra in palavra:
        if letra in lista_vogais:
            string = palavra.remove(letra)
            palavra = string
    return string