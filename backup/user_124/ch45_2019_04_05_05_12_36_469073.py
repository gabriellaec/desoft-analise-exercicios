def zera_negativos(valor):
	contador = 0
    while contador < len(valor):
        if valores[contador] < 0:
            valores[contador] = 0
        contador += 1

        