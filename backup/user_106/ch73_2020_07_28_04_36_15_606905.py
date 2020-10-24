def remove_vogais(texto):
    novo = ''
    for i in texto:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        else:    
            novo += i
    return novo

pal = 'abacate'

print(remove_vogais(pal))