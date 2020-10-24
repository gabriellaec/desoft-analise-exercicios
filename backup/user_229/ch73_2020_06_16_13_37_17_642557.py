def remove_vogais(string):
    nova_string = ''
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in string:
        if letra not in lista_vogais:
            nova_string += letra
    return nova_string