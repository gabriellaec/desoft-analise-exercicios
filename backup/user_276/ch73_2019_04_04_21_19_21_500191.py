def remove_vogais(string):
    i = 0
    sem_vogais = ''
    while i < len(string):
        if string[i] != 'a' or 'e' or 'i' or 'o' or 'u':
            sem_vogais += string[i]
    return string