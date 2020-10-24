def capitaliza(string):
    maiuscula = string.upper()
    lista = list(maiuscula)
    for i in range (1, len(lista)):
	    lista[i] = lista[i].lower()
    final = ''.join(lista)
    final_str = str(final)
    return final_str
    