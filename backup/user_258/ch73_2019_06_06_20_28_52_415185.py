def remove_vogais(string):
    string_sem_vogais = ''
    for k in string:
        if k != 'a' and k != 'e' and k != 'i' and k != 'o' and k != 'u':
            string_sem_vogais += k
    return string_sem_vogais