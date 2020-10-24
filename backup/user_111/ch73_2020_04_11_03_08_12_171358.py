import string
def remove_vogais(cad):
    vogais = 'aeiou'
    for ch in vogais:
        cad = string.replace(cad,ch,' ')
    return cad
