import string
def retira_vogais(cad):
    vogais = 'aeiou'
    for ch in vogais:
        cad = string.replace(cad,ch,' ')
    return cad
