#criando a função e delimitando o parâmetro lista
def zera_negativos(lista)
	nova_lista= lista
    i = 0
#iniciando o loop para que o procedimento se repita na cond. determinada
    while i < len(lista) - 1:
        #quando qualquer termo i da nova lista for menor do que 0, deve ser zerado
        if nova_lista [i] < 0:
            nova_lista [i]= 0
		i+= 1
	return nova_lista