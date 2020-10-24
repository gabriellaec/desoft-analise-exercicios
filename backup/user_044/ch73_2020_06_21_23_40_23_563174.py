def remove_vogais(string):
    stg = ''
    for i in string:
        if i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u':
            stg += i
    if stg == '':
        stg = False
    return stg
            