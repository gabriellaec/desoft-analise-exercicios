def lista_caracteres(palavra):
    listoberas=[]
    for e in palavra:
        if e not in listoberas:
        	listoberas.append(e)
    return listoberas
        