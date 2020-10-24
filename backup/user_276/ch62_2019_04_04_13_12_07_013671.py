def filtra_positivos(lista):
	lista_sem_neg = []
    i = 1
    while i < len(lista):
        if lista[i] > 0:
            lista_sem_neg.append(lista[i])
	return lista_sem_neg