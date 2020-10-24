def aniversariantes_de_setembro(n):
	d={}
	for nome,data in n.itens():
    	if data [3:5]== "9":
        	d[nome]=data
    return d
                