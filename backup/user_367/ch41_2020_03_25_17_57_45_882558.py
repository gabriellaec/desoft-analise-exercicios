def zera_negativos(lista):
    i=0
    while i < len(lista):
        if valores[i] < 0:
            valores[i] = 0
		i += 1
print(valores)