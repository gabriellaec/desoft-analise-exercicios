def apaga_repetidos(palavra):
    palavra_lista = list(palavra)
    nova_palavra = []

    for i in palavra_lista:
        if i.lower() not in nova_palavra:
            nova_palavra.append(i)
        elif i.lower() in nova_palavra:
            nova_palavra.append('*')

    palavra = ''.join(nova_palavra)

    return palavra

