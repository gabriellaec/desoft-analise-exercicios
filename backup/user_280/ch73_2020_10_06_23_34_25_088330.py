def remove_vogais(string):
    palavra = ''
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i] not in lista_vogais:
            palavra += string[i]
    return palavra