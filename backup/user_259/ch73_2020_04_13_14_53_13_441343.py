def remove_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    i = 0
    palavra1 = ''
    while i<len(palavra):
        if palavra[i] not in vogais:
            palavra1+=palavra[i]
            i+=1
        else:
            i+=1
    return palavra1