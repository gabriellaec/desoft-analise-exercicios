def eh_crescente(lista):
	new_lista = []
	maior_termo = lista[0]
	new_lista.append(lista[0])        
	i = 1
	while i < len(lista):
		if maior_termo < lista[i]:
			new_lista.append(lista[i])
            maior_termo = lista[i]
        
            
		i = i + 1
	if len(new_lista)==len(lista):
		return True
	else:
		return False