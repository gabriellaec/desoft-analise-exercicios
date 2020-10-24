letras.islower=True
def remove_vogais(letras):
    if 'a' in letras:
        del 'a'
    if 'e' in letras:
        del 'e'
    if 'i' in letras:
        del 'i'
    if 'o' in letras:
        del 'o'
    if 'u' in letras:
        del 'u'
    letras.isupper=False
        