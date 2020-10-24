def remove_vogais(palavra):
    
    lista2 = ["a", "e", "i", "o", "u"]
    lista1 = []
    
    for e in palavra:
        if not e in lista2:
            lista1.append(e)
            
	palavra_nova = ''.join(lista1)
    
    return palavra_nova
    
        