def remove_vogais(texto):
    novo = ''
    vogais = ['a', 'e', 'i', 'o', 'u']
    for l in texto:
        if not l in vogais:
            novo += l
    return novo




'''
def remove_vogais(texto):
    novo = ''
    for i in texto:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            a = True
        else:    
            novo += i
    return novo
'''