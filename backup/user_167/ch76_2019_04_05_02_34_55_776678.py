def aniversariantes_de_setembro(n):
	d={}
	for nome,data in n.itens():
    	if data [3:5]== "09":
        	d[nome]=data
    return d
                