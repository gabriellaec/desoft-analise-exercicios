def remove_vogais(string):
    lista = []
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i] not in lista_vogais:
            lista.append(string[i])    
    palavra =  lista.join()
    return palavra