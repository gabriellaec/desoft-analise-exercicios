def remove_vogais(palavra):
    lista=[]
    vogais=['a', 'e', 'i', 'o', 'u']
    lista_final=[]
    for letra in palavra:
        lista.append(letra)
    for e in lista:
        if e not in vogais:
            lista_final.append(e)
    r="".join(lista_final)
    return r
print(remove_vogais('abobora'))

