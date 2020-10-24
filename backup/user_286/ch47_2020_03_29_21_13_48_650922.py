def estritamente_crescente (lista):
    lista_final = [lista[0]]
    for numero in lista:
        if numero != lista[-1]:
        	if lista_final[-1] < lista[lista.index(numero)]:
            	lista_final.append(numero)

    return lista_final