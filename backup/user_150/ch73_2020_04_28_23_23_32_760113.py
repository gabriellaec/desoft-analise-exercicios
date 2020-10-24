def remove_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E,', 'I', 'O', 'U']
    letras = []
    for letra in palavra:
        if letra not in vogais:
            letras.append(letra)
    return ''.join(letras)