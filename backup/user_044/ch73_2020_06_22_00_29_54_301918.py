def remove_vogais(string):
    stg = ''
    for i in string:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            stg += i
    return stg
            