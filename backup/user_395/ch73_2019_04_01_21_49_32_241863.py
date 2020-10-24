def remove_vogais(string):
    palavra = ''
    for e in string:
        if e != 'a' and e != 'e' and e!= 'i' and e != 'o' and e != 'u':
            return string
    return remove_vogais('dora')