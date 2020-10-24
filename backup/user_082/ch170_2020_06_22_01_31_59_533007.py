def apaga_repetidos(palavra):
    palavra_lista = list(palavra)
    nova_palavra = []

    for i in palavra_lista:
        if i not in nova_palavra:
            nova_palavra.append(i)
        elif i in nova_palavra:
            nova_palavra.append('*')

    palavra = ''.join(nova_palavra)

    return palavra
