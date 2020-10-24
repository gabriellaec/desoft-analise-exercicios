def remove_vogais(cad):
    vogais = 'aeiou'
    for ch in vogais:
        cad = cad.replace(ch,'')
    return cad
