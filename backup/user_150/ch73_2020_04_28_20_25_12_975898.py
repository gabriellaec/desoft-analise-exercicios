def remove_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E,', 'I', 'O', 'U']
    for letra in palavra:
        if letra in vogais:
            return palavra.replace(letra, '')