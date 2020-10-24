def remove_vogais (string):
    saida = ''
    for i in range(len(string)):
        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
            saida = saida + string[i]
    return saida
        