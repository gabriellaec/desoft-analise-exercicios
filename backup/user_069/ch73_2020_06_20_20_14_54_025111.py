def remove_vogais(palavra):

    vogais = ['a', 'e', 'i', 'o', 'u']
    nova_palavra = ''

    for letra in palavra:

        if not letra in vogais:
            nova_palavra += letra

    return nova_palavra